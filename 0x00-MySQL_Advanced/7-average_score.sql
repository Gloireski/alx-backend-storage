-- SQL script that creates a stored procedure ComputeAverageScoreForUser
-- computes and store the average score for a student
DELIMITER $$
CREATE PROCEDURE ComputeAverageScoreForUser(IN user_id INT)
BEGIN
	DECLARE avg_ float;
	SELECT AVG(score) INTO avg_ FROM corrections AS C WHERE C.user_id=user_id;
	-- INSERT INTO users(average_score) VALUES(avg_);
	UPDATE users SET average_score = avg_ WHERE id=user_id;
END;
$$
