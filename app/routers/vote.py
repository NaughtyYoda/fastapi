from fastapi import status, HTTPException, Depends, APIRouter
from ..database import get_db
from .. import oauth2, models, schemas
from sqlalchemy.orm import Session

router = APIRouter(prefix='/vote', tags=['Vote'])


@router.post('/')
def voting(vote: schemas.Vote, db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)):

    # check if the posts exists
    verify_post = db.query(models.Post).filter(models.Post.post_id == vote.post_id).first()

    if not verify_post:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Post with ID {vote.post_id} not found"
        )

    vote_query = db.query(models.Vote).filter(
        models.Vote.post_id == vote.post_id,
        models.Vote.user_id == current_user.user_id
    )

    found_vote = vote_query.first()

    if vote.vote_dir == 1:
        if found_vote:
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail=f"User {current_user.user_id} has already voted on post {vote.post_id}"
            )
        new_vote = models.Vote(post_id=vote.post_id, user_id=current_user.user_id)
        db.add(new_vote)
        db.commit()
        db.refresh(new_vote)
        return {"message": "vote added"}

    if vote.vote_dir == 0:
        if not found_vote:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND
            )
        vote_query.delete(synchronize_session=False)
        db.commit()
        return {"message": "vote deleted"}
