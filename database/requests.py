from database.models import async_session
from database.models import Cover
from sqlalchemy import select, update, delete, desc


async def set_cover(track_url, file_id):
    async with async_session() as session:
        cover = await session.scalar(select(Cover).where(Cover.track_url == track_url))
        
        if not cover:
            session.add(Cover(track_url=track_url, file_id=file_id))
            await session.commit()
            
async def set_custom_cover(track_url, file_id):
    async with async_session() as session:
        cover = await session.scalar(select(Cover).where(Cover.track_url == track_url))
        
        if not cover:
            session.add(Cover(track_url=track_url, file_id=file_id))
        else:
            cover.file_id = file_id
        
        await session.commit()
        
async def get_cover(track_url):
    async with async_session() as session:
        cover = await session.scalar(select(Cover).where(Cover.track_url == track_url))
        
        if cover:
            return cover.file_id
        if not cover:
            return None
        
async def delete_cover(track_url):
    async with async_session() as session:
        cover = await session.scalar(select(Cover).where(Cover.track_url == track_url))
        await session.delete(cover)
        await session.commit()