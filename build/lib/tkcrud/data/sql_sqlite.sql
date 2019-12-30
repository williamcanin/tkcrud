CREATE TABLE IF NOT EXISTS clients (
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	name TEXT(200),
	address TEXT(100),
	date_of_birth TEXT(13),
	sex TEXT(15),
	marital_status TEXT(20),
	rg TEXT(18),
	cpf TEXT(15),
	cell_phone TEXT(17),
	email TEXT(100)
);
