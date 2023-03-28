CREATE DEFINER=`root`@`localhost` PROCEDURE `score_create`(
	  in _score int,
    in _game_id int,
    in _score_user varchar(50)
)
BEGIN
	  insert into `scores`
    (`score_user`,
    `score`,
    `game_id`)
    values
    (_score_user,
    _score,
    _game_id);
END