from .. import schemas, models, oauth2
from sqlalchemy.orm import Session
from fastapi import status, HTTPException, Depends, APIRouter
from typing import List, Optional
from ..database import get_db
from sqlalchemy import func


router = APIRouter(prefix='/posts', tags=['Posts'])


@router.get("/", response_model=List[schemas.PostOut])
async def get_posts(db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user),
                    limit: int = 10, skip=0, search: Optional[str] = ""):

    #posts = db.query(models.Post).all()

    posts = db.query(models.Post, func.count(models.Vote.post_id).label("n_votes"))\
        .join(models.Vote, models.Vote.post_id == models.Post.post_id, isouter=True)\
        .group_by(models.Post.post_id)\
        .filter(models.Post.post_title.contains(search))\
        .limit(limit)\
        .offset(skip)\
        .all()

    return [{"post": post, "n_votes": votes} for post, votes in posts]


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=schemas.PostResponse)
def create_posts(post: schemas.PostCreate, db: Session = Depends(get_db),
                 current_user: int = Depends(oauth2.get_current_user)):

    new_post = models.Post(owner_id=current_user.user_id,  **post.dict())  # unpacks the dictionary

    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return new_post


@router.get("/{id}", response_model=schemas.PostOut)
async def get_post(id: int, db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)):

    post = db.query(models.Post, func.count(models.Vote.post_id).label("n_votes"))\
        .join(models.Vote, models.Vote.post_id == models.Post.post_id, isouter=True)\
        .group_by(models.Post.post_id)\
        .filter(models.Post.post_id == id).first()

    if not post:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"post with ID: {id} was not found"
        )

    # if current_user.user_id != post.owner_id:
    #     raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
    #                         detail=f"Not authorized to perform requested action.")
    return {"post": post[0], "n_votes": post[1]}


@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id: int, db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)):

    post_query = db.query(models.Post).filter(models.Post.post_id == id)
    filtered_post = post_query.first()

    if filtered_post is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"ID {id} not found")

    if current_user.user_id != filtered_post.owner_id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                            detail=f"Not authorized to perform requested action.")

    post_query.delete(synchronize_session=False)
    db.commit()


@router.put("/{id}", response_model=schemas.PostResponse)
def update_post(id: int, updated_post: schemas.PostCreate, db: Session = Depends(get_db),
                current_user: int = Depends(oauth2.get_current_user)):
    post_query = db.query(models.Post).filter(models.Post.post_id == id)
    filtered_post = post_query.first()
    if filtered_post is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"ID {id} not found")
    print(updated_post)

    if current_user.user_id != filtered_post.owner_id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                            detail=f"Not authorized to perform requested action.")

    post_query.update(updated_post.dict())
    db.commit()
    return post_query.first()


