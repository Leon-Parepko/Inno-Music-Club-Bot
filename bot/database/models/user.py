from bot.database.models.base_model import BaseModel

create_table_query = '''CREATE TABLE public.users(
    user_id 	INT 			PRIMARY KEY,
    chat_id 	INT 			UNIQUE 	NOT 	NULL,
	alias 		VARCHAR ( 50 ) 	UNIQUE 	NOT 	NULL,
    
    name 		VARCHAR ( 50 ) 			NOT 	NULL,	--first name
    surname 	VARCHAR ( 50 ) 			NOT 	NULL,	--second name
    patronymic 	VARCHAR ( 50 ) 			NOT 	NULL,	--third name
    sex			VARCHAR ( 50 ) 			NOT 	NULL,	--male, female ot user option
	email 		VARCHAR ( 255 ) UNIQUE 	NOT 	NULL,
	phone		INT						NOT 	NULL,
	from_inno	BOOL,

	created_at 	TIMESTAMP 				NOT 	NULL,
	updated_at 	TIMESTAMP 				NOT 	NULL,
	deleted_at 	TIMESTAMP 				DEFAULT NULL
	-- password VARCHAR ( 50 ) 	NOT NULL,
    -- last_login TIMESTAMP 
);'''


class UserModel(BaseModel):

    def getCreateTableQuery(self) -> str:
        return create_table_query
