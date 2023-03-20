CREATE DEFINER=`root`@`localhost` PROCEDURE `game_create`(
	IN _game_name varchar(100),
    IN _game_authors varchar(500)
)
BEGIN
	if _game_authors = "None" then
		INSERT INTO `gamedatabase`.`games`
		(`game_name`,
		`game_authors`)
		VALUES
		(
		_game_name,
		null);
	else
		INSERT INTO `gamedatabase`.`games`
		(`game_name`,
		`game_authors`)
		VALUES
		(
		_game_name,
		_game_authors);
	end if;
END