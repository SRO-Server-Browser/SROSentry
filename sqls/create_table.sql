CREATE TABLE Panel_Silvarya.dbo._Announcement_AI (
	ID int IDENTITY(1,1) NOT NULL,
	LogDate datetime DEFAULT GETDATE() NOT NULL,
	_message varchar(150) NOT NULL,
	TargetCharName varchar(20),
	TargetCharID int,
	_private bit DEFAULT 0 NOT NULL,
	Processed bit DEFAULT 0 NOT NULL
);
