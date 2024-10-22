from bson import ObjectId
def sync_favorites(db_redis, user_col,  user):
    redis_key = f"user:{user['_id']}:favorites"
    
    favorite_strings = db_redis.smembers(redis_key)

    favorites = [eval(fav.decode('utf-8')) for fav in favorite_strings]

    user_col.update_one({'_id': ObjectId(user['_id'])}, {'$set': {'favoritos': favorites}})
    
    print("Sincronização com o MongoDB realizada com sucesso!")
