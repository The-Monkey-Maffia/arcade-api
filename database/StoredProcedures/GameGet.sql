CREATE DEFINER=`root`@`localhost` PROCEDURE `game_get`(
	in _id INT,
	in _game_name VARCHAR(100),
    in _game_authors VARCHAR(100)
)
BEGIN
	if _id is not null then
		SELECT * FROM gamedatabase.games
        WHERE game_id = _id;
	elseif _game_name is not null then
		SELECT * FROM gamedatabase.games
        WHERE game_name = _game_name;
	else
		SELECT * FROM gamedatabase.games
        WHERE game_authors LIKE _game_authors;
    end if;
END