CREATE DEFINER=`root`@`localhost` PROCEDURE `game_upsert`(
    in _id INT,
    in _game_name varchar(100),
    in _game_authors varchar(500)
)
BEGIN
	if _id is null then
		INSERT INTO `gamedatabase`.`games`
		(`game_name`,
		`game_authors`)
		VALUES
		(
		_game_name,
		_game_authors);
	else
		if _game_name is null then
			UPDATE `gamedatabase`.`games`
			SET
			`game_authors` = _game_authors
			WHERE `game_id` = _id;
		elseif _game_authors is null then
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
	end if;
END