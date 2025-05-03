SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
-- =============================================
-- Author:		SamsungA31
-- Create date: 03.05.2025
-- =============================================
CREATE PROCEDURE _SendMessage_FromAI
	@from_message_id int,
	@msg varchar(250)
AS
BEGIN
	DECLARE @bot_name varchar(100) = 'SamsungA31';
	DECLARE @target_char_name varchar(20);
	DECLARE @target_char_id int;

	IF EXISTS (
		SELECT 1 FROM Panel_Silvarya.dbo._Announcement_AI 
		WHERE _private = 1 AND ID = @from_message_id AND @from_message_id IS NOT NULL
	)
	BEGIN
		SELECT 
			@target_char_id = TargetCharID,
			@target_char_name = TargetCharName 
		FROM Panel_Silvarya.dbo._Announcement_AI 
		WHERE ID = @from_message_id;

		-- Private mesaj
		-- KGuardEdge
		INSERT INTO KGuardEDGE.dbo._DeveloperCommands (Cmd, Data1, Data2, Data3)
		VALUES ('private_sendpm', @target_char_name, @bot_name, @msg);
	END
	ELSE
	BEGIN
		-- Genel mesaj
		-- KGuardEdge
		INSERT INTO KGuardEDGE.dbo._DeveloperCommands (Cmd, Data1, Data2)
		VALUES ('server_sendpm', @bot_name, @msg);
	END
END;
