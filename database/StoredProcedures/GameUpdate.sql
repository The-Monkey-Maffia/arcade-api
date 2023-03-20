CREATE DEFINER=`root`@`localhost` PROCEDURE `game_update`(
    in _id INT,
    in _game_name varchar(100),
    in _game_authors varchar(500)
)
BEGIN
	if _game_name = "None" then
		UPDATE `gamedatabase`.`games`
		SET
		`game_authors` = _game_authors
		WHERE `game_id` = _id;
	elseif _game_authors = "None" then
		UPDATE `gamedatabase`.`games`
		SET
		`game_name` =  _game_name
		WHERE `game_id` = _id;
	else 
		UPDATE `gamedatabase`.`games`
		SET
		`game_name` =  _game_name,
		`game_authors` = _game_authors
		WHERE `game_id` = _id;
	end if;
END