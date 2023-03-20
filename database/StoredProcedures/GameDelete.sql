CREATE DEFINER=`root`@`localhost` PROCEDURE `game_delete`(
	in _id INT,
	in _GameName VARCHAR(100)
)
BEGIN
	if _id is null then
		DELETE FROM `gamedatabase`.`games`
		WHERE id=_id;
	else
		DELETE FROM `gamedatabase`.`games`
		WHERE GameName=_GameName;
    end if;
END