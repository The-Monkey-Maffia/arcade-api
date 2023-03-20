CREATE DEFINER=`root`@`localhost` PROCEDURE `score_get`(
    in _game_id varchar(100),
	in _score_user varchar(50),
    in _limit int
)
BEGIN
	if _limit = "None" or _limit is null then
		if _score_user = "None" or _score_user is null then
			select * from scores
			where game_id = _game_id;
		else
			select * from scores
			where game_id = _game_id and score_user = _score_user ;
		end if;
    else
		if _score_user = "None" or _score_user is null then
			select * from scores
			where game_id = _game_id
			limit _limit;
		else
			select * from scores
			where game_id = _game_id and score_user = _score_user
			limit _limit;
		end if;
	end if;
END