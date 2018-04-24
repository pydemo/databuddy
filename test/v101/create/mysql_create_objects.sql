drop table Date_test_to;

create table Date_test_to (
Id Int,
	Title varchar(64),	
	Isin  varchar(16),	
	Country varchar(64),	
	Description varchar(128),	
	SecurityType varchar(16),
	Created date);

drop table Date_test_from;
	
create table Date_test_from (
Id Int,
	Title varchar(64),	
	Isin  varchar(16),	
	Country varchar(64),	
	Description varchar(128),	
	SecurityType varchar(16),
	Created date);
	
	
insert into Date_test_from values(1,'Intel Corp.',	'US4581401001',	'United States',	'Equity, ISIN US4581401001, WKN 855681, INL',	'Equity', now());	
insert into Date_test_from values(2,'INTEL.COMMUN.NEW DL-,0001',	'US45824F2048',	'United States',	'Equity, ISIN US45824F2048, WKN A1CSQX, B3CN',	'Equity', now());
insert into Date_test_from values(3,'MICROSOFT 09/14',	'US594918AB00',	'United States',	'Bond, ISIN US594918AB00, WKN A0T922',	'Bond', now());
insert into Date_test_from values(4,'MICROSOFT 09/19',	'US594918AC82',	'United States',	'Bond, ISIN US594918AC82, WKN A0T923',	'Bond', now());
insert into Date_test_from values(5,'MICROSOFT 10/20',	'US594918AH79',	'United States',	'Bond, ISIN US594918AH79, WKN A1A1TC',	'Bond', now());
insert into Date_test_from values(6,'IBM CORP. 08-11 MTN',	'CH0042308749',	'Switzerland',	'Bond, ISIN CH0042308749, WKN A0TVDX',	'Bond', now());
insert into Date_test_from values(7,'IBM INTL GRP C. 2012',	'US44924EAB65',	'United States',	'Bond, ISIN US44924EAB65, WKN A0TLJY',	'Bond', now() );
insert into Date_test_from values(8,'IBM CORP. 08-15 MTN',	'CH0042308780',	'Switzerland',	'Bond, ISIN CH0042308780, WKN A0TVEN',	'Bond', now() );
insert into Date_test_from values(9,'Google Inc.',	'US38259P5089',	'US',	'Equity, ISIN US38259P5089, WKN A0B7FY, GGQ1',	'Equity', now() );
insert into Date_test_from values(10,'Capped Bonus Zertifikat auf Google',	'DE000CM6F7G6'	,'Germany',	'Investment Product, ISIN DE000CM6F7G6, WKN CM6F7G',	'Investment',  now() );
insert into Date_test_from values(11,'Capped Bonus Zertifikat auf Google',	'DE000CM6F7H4',	'Germany',	'Investment Product, ISIN DE000CM6F7H4, WKN CM6F7H',	'Investment', now() );
insert into Date_test_from values(12,'FACEBOOK INC',	'US30303M1027',	'UNITED STATES OF AMERICA',	'SHS FACEBOOK INC ORD REG',	'EQUITY', now() );

insert into Date_test_from values(13,'FACEBOOK INC',	'US30303M1027',	'UNITED STATES OF AMERICA',	'SHS FACEBOOK INC ORD BR',	'EQUITY', now() );
insert into Date_test_from values(14,'STRUCT CERT 25/09/12(FACEBOOK)USD17.7584',	'GB00B82JJN65',	'Great Britain - GB',	'STRUCT CERT 25/09/12(FACEBOOK)USD17.7584',	'Certificat', now() );
insert into Date_test_from values(15,'ORACLE 06/11',	'US68402LAE48',	'United States',	'Bond, ISIN US68402LAE48, WKN A0GUEX',	'Bond', now() );
insert into Date_test_from values(16,'ORACLE 09/14',	'US68389XAF24',	'United States',	'Bond, ISIN US68389XAF24, WKN A1AJTX',	'Bond', now() );
insert into Date_test_from values(17,'ORACLE 10/20 REGS',	'USU68308AA07',	'United States',	'Bond, ISIN USU68308AA07, WKN A1AY6N',	'Bond', now() );
insert into Date_test_from values(18,'BANK OF AMERICA 2016',	'US638585AU38',	'United States',	'Bond, ISIN US638585AU38, WKN 829067',	'Bond', now() );
insert into Date_test_from values(19,'BANK OF AMERICA 2028',	'US338915AH41',	'United States',	'Bond, ISIN US338915AH41, WKN 355410',	'Bond', now() );

insert into Date_test_from values(20,'BANK OF AMERICA 2028',	'US338915AM36',	'United States',	'Bond, ISIN US338915AM36, WKN 155239',	'Bond', now() );
insert into Date_test_from values(21,'MORGAN STANLEY 02/12MTN',	'US617446HC69',	'United States',	'Bond, ISIN US617446HC69, WKN 853722',	'Bond',now() );
insert into Date_test_from values(22,'MORGAN STANLEY 02/32MTN',	'US617446HD43',	'United States',	'Bond, ISIN US617446HD43, WKN 853723',	'Bond',now() );
insert into Date_test_from values(23,'MORGAN STANLEY 03/13MTN',	'US617446HS12',	'United States',	'Bond, ISIN US617446HS12, WKN 776381',	'Bond', now() );
insert into Date_test_from values(24,'CITIBANK N.A. 09/12',	'US17290CAB28',	'United States',	'Bond, ISIN US17290CAB28, WKN A1AHUG',	'Bond',now() );
insert into Date_test_from values(25,'CITIBANK N.A. 2011',	'US17314JAN37',	'United States',	'Bond, ISIN US17314JAN37, WKN A1AK2M',	'Bond',now() );
insert into Date_test_from values(26,'CITIBANK N.A. 2012',	'US17314JAT07',	'United States',	'Bond, ISIN US17314JAT07, WKN A1AN8G',	'Bond', now() );

insert into Date_test_from values(27,'COMCAST CAB.COM.HLD.02/13',	'US00209TAA34',	'United States',	'Bond, ISIN US00209TAA34, WKN 214099',	'Bond', now() );
insert into Date_test_from values(28,'COMCAST NEW 06/17',	'US20030NAP69',	'United States',	'Bond, ISIN US20030NAP69, WKN A0GVTR',	'Bond', now() );
insert into Date_test_from values(29,'COMCAST NEW 07/17',	'US20030NAU54',	'United States',	'Bond, ISIN US20030NAU54, WKN A0N11L',	'Bond',now() );
insert into Date_test_from values(30,'TRUVO SUBS. 04/14 REGS',	'XS0206614702',	'XS',	'Bond, ISIN XS0206614702, WKN A0DHDH',	'Bond',now() );
insert into Date_test_from values(31,'UBS (LUXEMB.) 06/16 REGS',	'XS0253861834',	'XS',	'Bond, ISIN XS0253861834, WKN A0GSAR',	'Bond',now() );
insert into Date_test_from values(32,'UBS (STAMFORD BR.) 10/12',	'US90261XGA46',	'United States',	'Bond, ISIN US90261XGA46, WKN A1AT4G',	'Bond', now() );
insert into Date_test_from values(33,'Deutsche Bank AG',	'DE0005140008',	'Germany',	'Equity, ISIN DE0005140008, WKN 514000, DBK',	'Equity',now() );

insert into Date_test_from values(34,'Aktien-Anleihe auf Deutsche Bank',	'DE000BLB8CL7',	'Germany',	'Investment Product, ISIN DE000BLB8CL7, WKN BLB8CL',	'Investment', now() );
insert into Date_test_from values(35,'Bonus-Zertifikat auf Deutsche Bank',	'DE000SG1ZT01',	'Germany',	'Investment Product, ISIN DE000SG1ZT01, WKN SG1ZT0',	'Investment', now() );
insert into Date_test_from values(36,'YAHOO JAPAN CORP.',	'JP3933800009',	'Japan',	'Equity, ISIN JP3933800009, WKN 916008, YOJ',	'Equity', now() );
insert into Date_test_from values(37,'Yahoo! Inc.',	'US9843321061',	'United States',	'Equity, ISIN US9843321061, WKN 900103, YHO',	'Equity', now() );
insert into Date_test_from values(38,'Discountzertifikat Classic auf Yahoo',	'DE000CM7YZ34',	'Germany',	'Investment Product, ISIN DE000CM7YZ34, WKN CM7YZ3',	'Investment', now() );
insert into Date_test_from values(39,'Allianz PIMCO Bondselect US $ - AT - USD',	'LU0035450757',	'Luxembourg',	'Funds, ISIN LU0035450757, WKN 971769, AZHL',	'Fund', now() );
insert into Date_test_from values(40,'Allianz PIMCO Bondspezial - A - EUR',	'LU0006245863',	'Luxembourg',	'Funds, ISIN LU0006245863, WKN 971114, DJED',	'Fund', now() );
insert into Date_test_from values(41,'Allianz PIMCO Convertible Bonds P',	'DE000A0ND6L9',	'Germany',	'Funds, ISIN DE000A0ND6L9, WKN A0ND6L, LQ6Q',	'Fund', now() );
insert into Date_test_from values(42,'CITCO TRUSTEES (CAYMAN) LIMITED',	'US17302TAA34',	'CAYMAN ISLANDS',	'USD 8,50 CITGO TRUSTEES CAYMAN(144A)04-2014',	'DEBT', now() );
insert into Date_test_from values(43,'CITCO TRUSTEES (CAYMAN) LIMITED',	'USG2149YAA40',	'CAYMAN ISLANDS',	'USD 8,50 CITGO TR. CAYMAN (REGS) 04-2014',	'DEBT', now() );


drop table Timestamp_test_to;
	
create table Timestamp_test_to (
Id Int,
	Title varchar(64),	
	Isin  varchar(16),	
	Country varchar(64),	
	Description varchar(128),	
	SecurityType varchar(16),
	Created timestamp NOT NULL DEFAULT now());

drop table Timestamp_test_from;
	
create table Timestamp_test_from (
Id Int,
	Title varchar(64),	
	Isin  varchar(16),	
	Country varchar(64),	
	Description varchar(128),	
	SecurityType varchar(16),
	Created timestamp NOT NULL DEFAULT now());



insert into Timestamp_test_from values(1,'Intel Corp.',	'US4581401001',	'United States',	'Equity, ISIN US4581401001, WKN 855681, INL',	'Equity', now());
insert into Timestamp_test_from values(1,'Intel Corp.',	'US4581401001',	'United States',	'Equity, ISIN US4581401001, WKN 855681, INL',	'Equity', now());
insert into Timestamp_test_from values(2,'INTEL.COMMUN.NEW DL-,0001',	'US45824F2048',	'United States',	'Equity, ISIN US45824F2048, WKN A1CSQX, B3CN',	'Equity', now());
insert into Timestamp_test_from values(3,'MICROSOFT 09/14',	'US594918AB00',	'United States',	'Bond, ISIN US594918AB00, WKN A0T922',	'Bond', now());
insert into Timestamp_test_from values(4,'MICROSOFT 09/19',	'US594918AC82',	'United States',	'Bond, ISIN US594918AC82, WKN A0T923',	'Bond', now());
insert into Timestamp_test_from values(5,'MICROSOFT 10/20',	'US594918AH79',	'United States',	'Bond, ISIN US594918AH79, WKN A1A1TC',	'Bond', now());
insert into Timestamp_test_from values(6,'IBM CORP. 08-11 MTN',	'CH0042308749',	'Switzerland',	'Bond, ISIN CH0042308749, WKN A0TVDX',	'Bond', now());
insert into Timestamp_test_from values(7,'IBM INTL GRP C. 2012',	'US44924EAB65',	'United States',	'Bond, ISIN US44924EAB65, WKN A0TLJY',	'Bond', now() );
insert into Timestamp_test_from values(8,'IBM CORP. 08-15 MTN',	'CH0042308780',	'Switzerland',	'Bond, ISIN CH0042308780, WKN A0TVEN',	'Bond', now() );
insert into Timestamp_test_from values(9,'Google Inc.',	'US38259P5089',	'US',	'Equity, ISIN US38259P5089, WKN A0B7FY, GGQ1',	'Equity', now() );
insert into Timestamp_test_from values(10,'Capped Bonus Zertifikat auf Google',	'DE000CM6F7G6'	,'Germany',	'Investment Product, ISIN DE000CM6F7G6, WKN CM6F7G',	'Investment',  now() );
insert into Timestamp_test_from values(11,'Capped Bonus Zertifikat auf Google',	'DE000CM6F7H4',	'Germany',	'Investment Product, ISIN DE000CM6F7H4, WKN CM6F7H',	'Investment', now() );
insert into Timestamp_test_from values(12,'FACEBOOK INC',	'US30303M1027',	'UNITED STATES OF AMERICA',	'SHS FACEBOOK INC ORD REG',	'EQUITY', now() );

insert into Timestamp_test_from values(13,'FACEBOOK INC',	'US30303M1027',	'UNITED STATES OF AMERICA',	'SHS FACEBOOK INC ORD BR',	'EQUITY', now() );
insert into Timestamp_test_from values(14,'STRUCT CERT 25/09/12(FACEBOOK)USD17.7584',	'GB00B82JJN65',	'Great Britain - GB',	'STRUCT CERT 25/09/12(FACEBOOK)USD17.7584',	'Certificat', now() );
insert into Timestamp_test_from values(15,'ORACLE 06/11',	'US68402LAE48',	'United States',	'Bond, ISIN US68402LAE48, WKN A0GUEX',	'Bond', now() );
insert into Timestamp_test_from values(16,'ORACLE 09/14',	'US68389XAF24',	'United States',	'Bond, ISIN US68389XAF24, WKN A1AJTX',	'Bond', now() );
insert into Timestamp_test_from values(17,'ORACLE 10/20 REGS',	'USU68308AA07',	'United States',	'Bond, ISIN USU68308AA07, WKN A1AY6N',	'Bond', now() );
insert into Timestamp_test_from values(18,'BANK OF AMERICA 2016',	'US638585AU38',	'United States',	'Bond, ISIN US638585AU38, WKN 829067',	'Bond', now() );
insert into Timestamp_test_from values(19,'BANK OF AMERICA 2028',	'US338915AH41',	'United States',	'Bond, ISIN US338915AH41, WKN 355410',	'Bond', now() );

insert into Timestamp_test_from values(20,'BANK OF AMERICA 2028',	'US338915AM36',	'United States',	'Bond, ISIN US338915AM36, WKN 155239',	'Bond', now() );
insert into Timestamp_test_from values(21,'MORGAN STANLEY 02/12MTN',	'US617446HC69',	'United States',	'Bond, ISIN US617446HC69, WKN 853722',	'Bond',now() );
insert into Timestamp_test_from values(22,'MORGAN STANLEY 02/32MTN',	'US617446HD43',	'United States',	'Bond, ISIN US617446HD43, WKN 853723',	'Bond',now() );
insert into Timestamp_test_from values(23,'MORGAN STANLEY 03/13MTN',	'US617446HS12',	'United States',	'Bond, ISIN US617446HS12, WKN 776381',	'Bond', now() );
insert into Timestamp_test_from values(24,'CITIBANK N.A. 09/12',	'US17290CAB28',	'United States',	'Bond, ISIN US17290CAB28, WKN A1AHUG',	'Bond',now() );
insert into Timestamp_test_from values(25,'CITIBANK N.A. 2011',	'US17314JAN37',	'United States',	'Bond, ISIN US17314JAN37, WKN A1AK2M',	'Bond',now() );
insert into Timestamp_test_from values(26,'CITIBANK N.A. 2012',	'US17314JAT07',	'United States',	'Bond, ISIN US17314JAT07, WKN A1AN8G',	'Bond', now() );

insert into Timestamp_test_from values(27,'COMCAST CAB.COM.HLD.02/13',	'US00209TAA34',	'United States',	'Bond, ISIN US00209TAA34, WKN 214099',	'Bond', now() );
insert into Timestamp_test_from values(28,'COMCAST NEW 06/17',	'US20030NAP69',	'United States',	'Bond, ISIN US20030NAP69, WKN A0GVTR',	'Bond', now() );
insert into Timestamp_test_from values(29,'COMCAST NEW 07/17',	'US20030NAU54',	'United States',	'Bond, ISIN US20030NAU54, WKN A0N11L',	'Bond',now() );
insert into Timestamp_test_from values(30,'TRUVO SUBS. 04/14 REGS',	'XS0206614702',	'XS',	'Bond, ISIN XS0206614702, WKN A0DHDH',	'Bond',now() );
insert into Timestamp_test_from values(31,'UBS (LUXEMB.) 06/16 REGS',	'XS0253861834',	'XS',	'Bond, ISIN XS0253861834, WKN A0GSAR',	'Bond',now() );
insert into Timestamp_test_from values(32,'UBS (STAMFORD BR.) 10/12',	'US90261XGA46',	'United States',	'Bond, ISIN US90261XGA46, WKN A1AT4G',	'Bond', now() );
insert into Timestamp_test_from values(33,'Deutsche Bank AG',	'DE0005140008',	'Germany',	'Equity, ISIN DE0005140008, WKN 514000, DBK',	'Equity',now() );

insert into Timestamp_test_from values(34,'Aktien-Anleihe auf Deutsche Bank',	'DE000BLB8CL7',	'Germany',	'Investment Product, ISIN DE000BLB8CL7, WKN BLB8CL',	'Investment', now() );
insert into Timestamp_test_from values(35,'Bonus-Zertifikat auf Deutsche Bank',	'DE000SG1ZT01',	'Germany',	'Investment Product, ISIN DE000SG1ZT01, WKN SG1ZT0',	'Investment', now() );
insert into Timestamp_test_from values(36,'YAHOO JAPAN CORP.',	'JP3933800009',	'Japan',	'Equity, ISIN JP3933800009, WKN 916008, YOJ',	'Equity', now() );
insert into Timestamp_test_from values(37,'Yahoo! Inc.',	'US9843321061',	'United States',	'Equity, ISIN US9843321061, WKN 900103, YHO',	'Equity', now() );
insert into Timestamp_test_from values(38,'Discountzertifikat Classic auf Yahoo',	'DE000CM7YZ34',	'Germany',	'Investment Product, ISIN DE000CM7YZ34, WKN CM7YZ3',	'Investment', now() );
insert into Timestamp_test_from values(39,'Allianz PIMCO Bondselect US $ - AT - USD',	'LU0035450757',	'Luxembourg',	'Funds, ISIN LU0035450757, WKN 971769, AZHL',	'Fund', now() );
insert into Timestamp_test_from values(40,'Allianz PIMCO Bondspezial - A - EUR',	'LU0006245863',	'Luxembourg',	'Funds, ISIN LU0006245863, WKN 971114, DJED',	'Fund', now() );
insert into Timestamp_test_from values(41,'Allianz PIMCO Convertible Bonds P',	'DE000A0ND6L9',	'Germany',	'Funds, ISIN DE000A0ND6L9, WKN A0ND6L, LQ6Q',	'Fund', now() );
insert into Timestamp_test_from values(42,'CITCO TRUSTEES (CAYMAN) LIMITED',	'US17302TAA34',	'CAYMAN ISLANDS',	'USD 8,50 CITGO TRUSTEES CAYMAN(144A)04-2014',	'DEBT', now() );
insert into Timestamp_test_from values(43,'CITCO TRUSTEES (CAYMAN) LIMITED',	'USG2149YAA40',	'CAYMAN ISLANDS',	'USD 8,50 CITGO TR. CAYMAN (REGS) 04-2014',	'DEBT', now() );


drop table Timezone_test_to;


create table Timezone_test_to (
Id Int,
	Title varchar(64),	
	Isin  varchar(16),	
	Country varchar(64),	
	Description varchar(128),	
	SecurityType varchar(16),
	Created timestamp,
	Timezone varchar(8));

drop table Timezone_test_from;
	
create table Timezone_test_from (
Id Int,
	Title varchar(64),	
	Isin  varchar(16),	
	Country varchar(64),	
	Description varchar(128),	
	SecurityType varchar(16),
	Created timestamp,
	Timezone varchar(8));

	
insert into Timezone_test_from values(1,'Intel Corp.',	'US4581401001',	'United States',	'Equity, ISIN US4581401001, WKN 855681, INL',	'Equity', now(),'-04:00');
insert into Timezone_test_from values(2,'INTEL.COMMUN.NEW DL-,0001',	'US45824F2048',	'United States',	'Equity, ISIN US45824F2048, WKN A1CSQX, B3CN',	'Equity', now(),'-04:00');
insert into Timezone_test_from values(3,'MICROSOFT 09/14',	'US594918AB00',	'United States',	'Bond, ISIN US594918AB00, WKN A0T922',	'Bond', now(),'-04:00');
insert into Timezone_test_from values(4,'MICROSOFT 09/19',	'US594918AC82',	'United States',	'Bond, ISIN US594918AC82, WKN A0T923',	'Bond', now(),'-04:00');
insert into Timezone_test_from values(5,'MICROSOFT 10/20',	'US594918AH79',	'United States',	'Bond, ISIN US594918AH79, WKN A1A1TC',	'Bond', now(),'-04:00');
insert into Timezone_test_from values(6,'IBM CORP. 08-11 MTN',	'CH0042308749',	'Switzerland',	'Bond, ISIN CH0042308749, WKN A0TVDX',	'Bond', now(),'-04:00');
insert into Timezone_test_from values(7,'IBM INTL GRP C. 2012',	'US44924EAB65',	'United States',	'Bond, ISIN US44924EAB65, WKN A0TLJY',	'Bond', now() ,'-04:00'));
insert into Timezone_test_from values(8,'IBM CORP. 08-15 MTN',	'CH0042308780',	'Switzerland',	'Bond, ISIN CH0042308780, WKN A0TVEN',	'Bond', now() ,'-04:00'));
insert into Timezone_test_from values(9,'Google Inc.',	'US38259P5089',	'US',	'Equity, ISIN US38259P5089, WKN A0B7FY, GGQ1',	'Equity', now() ,'-04:00'));
insert into Timezone_test_from values(10,'Capped Bonus Zertifikat auf Google',	'DE000CM6F7G6'	,'Germany',	'Investment Product, ISIN DE000CM6F7G6, WKN CM6F7G',	'Investment',  now() ,'-04:00');
insert into Timezone_test_from values(11,'Capped Bonus Zertifikat auf Google',	'DE000CM6F7H4',	'Germany',	'Investment Product, ISIN DE000CM6F7H4, WKN CM6F7H',	'Investment', now() ,'-04:00');
insert into Timezone_test_from values(12,'FACEBOOK INC',	'US30303M1027',	'UNITED STATES OF AMERICA',	'SHS FACEBOOK INC ORD REG',	'EQUITY', now() ,'-04:00');

insert into Timezone_test_from values(13,'FACEBOOK INC',	'US30303M1027',	'UNITED STATES OF AMERICA',	'SHS FACEBOOK INC ORD BR',	'EQUITY', now() ,'-04:00');
insert into Timezone_test_from values(14,'STRUCT CERT 25/09/12(FACEBOOK)USD17.7584',	'GB00B82JJN65',	'Great Britain - GB',	'STRUCT CERT 25/09/12(FACEBOOK)USD17.7584',	'Certificat', now() ,'-04:00');
insert into Timezone_test_from values(15,'ORACLE 06/11',	'US68402LAE48',	'United States',	'Bond, ISIN US68402LAE48, WKN A0GUEX',	'Bond', now() ,'-04:00');
insert into Timezone_test_from values(16,'ORACLE 09/14',	'US68389XAF24',	'United States',	'Bond, ISIN US68389XAF24, WKN A1AJTX',	'Bond', now() ,'-04:00');
insert into Timezone_test_from values(17,'ORACLE 10/20 REGS',	'USU68308AA07',	'United States',	'Bond, ISIN USU68308AA07, WKN A1AY6N',	'Bond', now() ,'-04:00');
insert into Timezone_test_from values(18,'BANK OF AMERICA 2016',	'US638585AU38',	'United States',	'Bond, ISIN US638585AU38, WKN 829067',	'Bond', now() ,'-04:00');
insert into Timezone_test_from values(19,'BANK OF AMERICA 2028',	'US338915AH41',	'United States',	'Bond, ISIN US338915AH41, WKN 355410',	'Bond', now() ,'-04:00');

insert into Timezone_test_from values(20,'BANK OF AMERICA 2028',	'US338915AM36',	'United States',	'Bond, ISIN US338915AM36, WKN 155239',	'Bond', now() ,'-04:00');
insert into Timezone_test_from values(21,'MORGAN STANLEY 02/12MTN',	'US617446HC69',	'United States',	'Bond, ISIN US617446HC69, WKN 853722',	'Bond',now() ,'-04:00');
insert into Timezone_test_from values(22,'MORGAN STANLEY 02/32MTN',	'US617446HD43',	'United States',	'Bond, ISIN US617446HD43, WKN 853723',	'Bond',now() ,'-04:00');
insert into Timezone_test_from values(23,'MORGAN STANLEY 03/13MTN',	'US617446HS12',	'United States',	'Bond, ISIN US617446HS12, WKN 776381',	'Bond', now() ,'-04:00');
insert into Timezone_test_from values(24,'CITIBANK N.A. 09/12',	'US17290CAB28',	'United States',	'Bond, ISIN US17290CAB28, WKN A1AHUG',	'Bond',now() ,'-04:00');
insert into Timezone_test_from values(25,'CITIBANK N.A. 2011',	'US17314JAN37',	'United States',	'Bond, ISIN US17314JAN37, WKN A1AK2M',	'Bond',now() ,'-04:00');
insert into Timezone_test_from values(26,'CITIBANK N.A. 2012',	'US17314JAT07',	'United States',	'Bond, ISIN US17314JAT07, WKN A1AN8G',	'Bond', now() ,'-04:00');

insert into Timezone_test_from values(27,'COMCAST CAB.COM.HLD.02/13',	'US00209TAA34',	'United States',	'Bond, ISIN US00209TAA34, WKN 214099',	'Bond', now() ,'-04:00');
insert into Timezone_test_from values(28,'COMCAST NEW 06/17',	'US20030NAP69',	'United States',	'Bond, ISIN US20030NAP69, WKN A0GVTR',	'Bond', now() ,'-04:00');
insert into Timezone_test_from values(29,'COMCAST NEW 07/17',	'US20030NAU54',	'United States',	'Bond, ISIN US20030NAU54, WKN A0N11L',	'Bond',now() ,'-04:00');
insert into Timezone_test_from values(30,'TRUVO SUBS. 04/14 REGS',	'XS0206614702',	'XS',	'Bond, ISIN XS0206614702, WKN A0DHDH',	'Bond',now() ,'-04:00');
insert into Timezone_test_from values(31,'UBS (LUXEMB.) 06/16 REGS',	'XS0253861834',	'XS',	'Bond, ISIN XS0253861834, WKN A0GSAR',	'Bond',now() ,'-04:00');
insert into Timezone_test_from values(32,'UBS (STAMFORD BR.) 10/12',	'US90261XGA46',	'United States',	'Bond, ISIN US90261XGA46, WKN A1AT4G',	'Bond', now() ,'-04:00');
insert into Timezone_test_from values(33,'Deutsche Bank AG',	'DE0005140008',	'Germany',	'Equity, ISIN DE0005140008, WKN 514000, DBK',	'Equity',now() ,'-04:00');

insert into Timezone_test_from values(34,'Aktien-Anleihe auf Deutsche Bank',	'DE000BLB8CL7',	'Germany',	'Investment Product, ISIN DE000BLB8CL7, WKN BLB8CL',	'Investment', now() ,'-04:00');
insert into Timezone_test_from values(35,'Bonus-Zertifikat auf Deutsche Bank',	'DE000SG1ZT01',	'Germany',	'Investment Product, ISIN DE000SG1ZT01, WKN SG1ZT0',	'Investment', now() ,'-04:00');
insert into Timezone_test_from values(36,'YAHOO JAPAN CORP.',	'JP3933800009',	'Japan',	'Equity, ISIN JP3933800009, WKN 916008, YOJ',	'Equity', now() ,'-04:00');
insert into Timezone_test_from values(37,'Yahoo! Inc.',	'US9843321061',	'United States',	'Equity, ISIN US9843321061, WKN 900103, YHO',	'Equity', now() ,'-04:00');
insert into Timezone_test_from values(38,'Discountzertifikat Classic auf Yahoo',	'DE000CM7YZ34',	'Germany',	'Investment Product, ISIN DE000CM7YZ34, WKN CM7YZ3',	'Investment', now() ,'-04:00');
insert into Timezone_test_from values(39,'Allianz PIMCO Bondselect US $ - AT - USD',	'LU0035450757',	'Luxembourg',	'Funds, ISIN LU0035450757, WKN 971769, AZHL',	'Fund', now() ,'-04:00');
insert into Timezone_test_from values(40,'Allianz PIMCO Bondspezial - A - EUR',	'LU0006245863',	'Luxembourg',	'Funds, ISIN LU0006245863, WKN 971114, DJED',	'Fund', now() ,'-04:00');
insert into Timezone_test_from values(41,'Allianz PIMCO Convertible Bonds P',	'DE000A0ND6L9',	'Germany',	'Funds, ISIN DE000A0ND6L9, WKN A0ND6L, LQ6Q',	'Fund', now() ,'-04:00');
insert into Timezone_test_from values(42,'CITCO TRUSTEES (CAYMAN) LIMITED',	'US17302TAA34',	'CAYMAN ISLANDS',	'USD 8,50 CITGO TRUSTEES CAYMAN(144A)04-2014',	'DEBT', now() ,'-04:00');
insert into Timezone_test_from values(43,'CITCO TRUSTEES (CAYMAN) LIMITED',	'USG2149YAA40',	'CAYMAN ISLANDS',	'USD 8,50 CITGO TR. CAYMAN (REGS) 04-2014',	'DEBT', now() ,'-04:00');


drop table Partitioned_test_from;

CREATE TABLE Partitioned_test_from
(
Id Int,
	Title varchar(64),	
	Isin  varchar(16),	
	Country varchar(64),	
	Description varchar(128),	
	SecurityType varchar(16),
	Created date
) ENGINE=InnoDB DEFAULT CHARSET=latin1
PARTITION BY RANGE( TO_DAYS(Created) ) (
PARTITION rx2014 VALUES LESS THAN( TO_DAYS('2014-01-01 00:00:00') ), 
PARTITION rx2015 VALUES LESS THAN( TO_DAYS('2015-01-01 00:00:00') ), 
PARTITION rx2016 VALUES LESS THAN( TO_DAYS('2016-01-01 00:00:00') ), 
PARTITION rxMORES VALUES LESS THAN (MAXVALUE) );


drop table Partitioned_test_to;

CREATE TABLE Partitioned_test_to
(
Id Int,
	Title varchar(64),	
	Isin  varchar(16),	
	Country varchar(64),	
	Description varchar(128),	
	SecurityType varchar(16),
	Created date
) ENGINE=InnoDB DEFAULT CHARSET=latin1
PARTITION BY RANGE( TO_DAYS(Created) ) (
PARTITION rx2014 VALUES LESS THAN( TO_DAYS('2014-01-01 00:00:00') ), 
PARTITION rx2015 VALUES LESS THAN( TO_DAYS('2015-01-01 00:00:00') ), 
PARTITION rx2016 VALUES LESS THAN( TO_DAYS('2016-01-01 00:00:00') ), 
PARTITION rxMORES VALUES LESS THAN (MAXVALUE) );



insert into Partitioned_test_from values(1,'Intel Corp.',	'US4581401001',	'United States',	'Equity, ISIN US4581401001, WKN 855681, INL',	'Equity', now());
insert into Partitioned_test_from values(2,'INTEL.COMMUN.NEW DL-,0001',	'US45824F2048',	'United States',	'Equity, ISIN US45824F2048, WKN A1CSQX, B3CN',	'Equity', now());
insert into Partitioned_test_from values(3,'MICROSOFT 09/14',	'US594918AB00',	'United States',	'Bond, ISIN US594918AB00, WKN A0T922',	'Bond', now());
insert into Partitioned_test_from values(4,'MICROSOFT 09/19',	'US594918AC82',	'United States',	'Bond, ISIN US594918AC82, WKN A0T923',	'Bond', now());
insert into Partitioned_test_from values(5,'MICROSOFT 10/20',	'US594918AH79',	'United States',	'Bond, ISIN US594918AH79, WKN A1A1TC',	'Bond', now());
insert into Partitioned_test_from values(6,'IBM CORP. 08-11 MTN',	'CH0042308749',	'Switzerland',	'Bond, ISIN CH0042308749, WKN A0TVDX',	'Bond', now());
insert into Partitioned_test_from values(7,'IBM INTL GRP C. 2012',	'US44924EAB65',	'United States',	'Bond, ISIN US44924EAB65, WKN A0TLJY',	'Bond', now() );
insert into Partitioned_test_from values(8,'IBM CORP. 08-15 MTN',	'CH0042308780',	'Switzerland',	'Bond, ISIN CH0042308780, WKN A0TVEN',	'Bond', now() );
insert into Partitioned_test_from values(9,'Google Inc.',	'US38259P5089',	'US',	'Equity, ISIN US38259P5089, WKN A0B7FY, GGQ1',	'Equity', now() );
insert into Partitioned_test_from values(10,'Capped Bonus Zertifikat auf Google',	'DE000CM6F7G6'	,'Germany',	'Investment Product, ISIN DE000CM6F7G6, WKN CM6F7G',	'Investment',  now() );
insert into Partitioned_test_from values(11,'Capped Bonus Zertifikat auf Google',	'DE000CM6F7H4',	'Germany',	'Investment Product, ISIN DE000CM6F7H4, WKN CM6F7H',	'Investment', now() );
insert into Partitioned_test_from values(12,'FACEBOOK INC',	'US30303M1027',	'UNITED STATES OF AMERICA',	'SHS FACEBOOK INC ORD REG',	'EQUITY', now() );

insert into Partitioned_test_from values(13,'FACEBOOK INC',	'US30303M1027',	'UNITED STATES OF AMERICA',	'SHS FACEBOOK INC ORD BR',	'EQUITY', now() );
insert into Partitioned_test_from values(14,'STRUCT CERT 25/09/12(FACEBOOK)USD17.7584',	'GB00B82JJN65',	'Great Britain - GB',	'STRUCT CERT 25/09/12(FACEBOOK)USD17.7584',	'Certificat', now() );
insert into Partitioned_test_from values(15,'ORACLE 06/11',	'US68402LAE48',	'United States',	'Bond, ISIN US68402LAE48, WKN A0GUEX',	'Bond', now() );
insert into Partitioned_test_from values(16,'ORACLE 09/14',	'US68389XAF24',	'United States',	'Bond, ISIN US68389XAF24, WKN A1AJTX',	'Bond', now() );
insert into Partitioned_test_from values(17,'ORACLE 10/20 REGS',	'USU68308AA07',	'United States',	'Bond, ISIN USU68308AA07, WKN A1AY6N',	'Bond', now() );
insert into Partitioned_test_from values(18,'BANK OF AMERICA 2016',	'US638585AU38',	'United States',	'Bond, ISIN US638585AU38, WKN 829067',	'Bond', now() );
insert into Partitioned_test_from values(19,'BANK OF AMERICA 2028',	'US338915AH41',	'United States',	'Bond, ISIN US338915AH41, WKN 355410',	'Bond', now() );

insert into Partitioned_test_from values(20,'BANK OF AMERICA 2028',	'US338915AM36',	'United States',	'Bond, ISIN US338915AM36, WKN 155239',	'Bond', now() );
insert into Partitioned_test_from values(21,'MORGAN STANLEY 02/12MTN',	'US617446HC69',	'United States',	'Bond, ISIN US617446HC69, WKN 853722',	'Bond',now() );
insert into Partitioned_test_from values(22,'MORGAN STANLEY 02/32MTN',	'US617446HD43',	'United States',	'Bond, ISIN US617446HD43, WKN 853723',	'Bond',now() );
insert into Partitioned_test_from values(23,'MORGAN STANLEY 03/13MTN',	'US617446HS12',	'United States',	'Bond, ISIN US617446HS12, WKN 776381',	'Bond', now() );
insert into Partitioned_test_from values(24,'CITIBANK N.A. 09/12',	'US17290CAB28',	'United States',	'Bond, ISIN US17290CAB28, WKN A1AHUG',	'Bond',now() );
insert into Partitioned_test_from values(25,'CITIBANK N.A. 2011',	'US17314JAN37',	'United States',	'Bond, ISIN US17314JAN37, WKN A1AK2M',	'Bond',now() );
insert into Partitioned_test_from values(26,'CITIBANK N.A. 2012',	'US17314JAT07',	'United States',	'Bond, ISIN US17314JAT07, WKN A1AN8G',	'Bond', now() );

insert into Partitioned_test_from values(27,'COMCAST CAB.COM.HLD.02/13',	'US00209TAA34',	'United States',	'Bond, ISIN US00209TAA34, WKN 214099',	'Bond', now() );
insert into Partitioned_test_from values(28,'COMCAST NEW 06/17',	'US20030NAP69',	'United States',	'Bond, ISIN US20030NAP69, WKN A0GVTR',	'Bond', now() );
insert into Partitioned_test_from values(29,'COMCAST NEW 07/17',	'US20030NAU54',	'United States',	'Bond, ISIN US20030NAU54, WKN A0N11L',	'Bond',now() );
insert into Partitioned_test_from values(30,'TRUVO SUBS. 04/14 REGS',	'XS0206614702',	'XS',	'Bond, ISIN XS0206614702, WKN A0DHDH',	'Bond',now() );
insert into Partitioned_test_from values(31,'UBS (LUXEMB.) 06/16 REGS',	'XS0253861834',	'XS',	'Bond, ISIN XS0253861834, WKN A0GSAR',	'Bond',now() );
insert into Partitioned_test_from values(32,'UBS (STAMFORD BR.) 10/12',	'US90261XGA46',	'United States',	'Bond, ISIN US90261XGA46, WKN A1AT4G',	'Bond', now() );
insert into Partitioned_test_from values(33,'Deutsche Bank AG',	'DE0005140008',	'Germany',	'Equity, ISIN DE0005140008, WKN 514000, DBK',	'Equity',now() );

insert into Partitioned_test_from values(34,'Aktien-Anleihe auf Deutsche Bank',	'DE000BLB8CL7',	'Germany',	'Investment Product, ISIN DE000BLB8CL7, WKN BLB8CL',	'Investment', now() );
insert into Partitioned_test_from values(35,'Bonus-Zertifikat auf Deutsche Bank',	'DE000SG1ZT01',	'Germany',	'Investment Product, ISIN DE000SG1ZT01, WKN SG1ZT0',	'Investment', now() );
insert into Partitioned_test_from values(36,'YAHOO JAPAN CORP.',	'JP3933800009',	'Japan',	'Equity, ISIN JP3933800009, WKN 916008, YOJ',	'Equity', now() );
insert into Partitioned_test_from values(37,'Yahoo! Inc.',	'US9843321061',	'United States',	'Equity, ISIN US9843321061, WKN 900103, YHO',	'Equity', now() );
insert into Partitioned_test_from values(38,'Discountzertifikat Classic auf Yahoo',	'DE000CM7YZ34',	'Germany',	'Investment Product, ISIN DE000CM7YZ34, WKN CM7YZ3',	'Investment', now() );
insert into Partitioned_test_from values(39,'Allianz PIMCO Bondselect US $ - AT - USD',	'LU0035450757',	'Luxembourg',	'Funds, ISIN LU0035450757, WKN 971769, AZHL',	'Fund', now() );
insert into Partitioned_test_from values(40,'Allianz PIMCO Bondspezial - A - EUR',	'LU0006245863',	'Luxembourg',	'Funds, ISIN LU0006245863, WKN 971114, DJED',	'Fund', now() );
insert into Partitioned_test_from values(41,'Allianz PIMCO Convertible Bonds P',	'DE000A0ND6L9',	'Germany',	'Funds, ISIN DE000A0ND6L9, WKN A0ND6L, LQ6Q',	'Fund', now() );
insert into Partitioned_test_from values(42,'CITCO TRUSTEES (CAYMAN) LIMITED',	'US17302TAA34',	'CAYMAN ISLANDS',	'USD 8,50 CITGO TRUSTEES CAYMAN(144A)04-2014',	'DEBT', now() );
insert into Partitioned_test_from values(43,'CITCO TRUSTEES (CAYMAN) LIMITED',	'USG2149YAA40',	'CAYMAN ISLANDS',	'USD 8,50 CITGO TR. CAYMAN (REGS) 04-2014',	'DEBT', now() );



CREATE TABLE Sub_Partitioned_test_to
(
Id Int,
	Title varchar(64),	
	Isin  varchar(16),	
	Country varchar(64),	
	Description varchar(128),	
	SecurityType varchar(16),
	Created date
) ENGINE=InnoDB DEFAULT CHARSET=latin1
PARTITION BY RANGE( TO_DAYS(Created) )
subpartition by hash (Id) (
PARTITION rx2014 VALUES LESS THAN( TO_DAYS('2014-01-01 00:00:00')) (SUBPARTITION subpart100, SUBPARTITION subpart101), 
PARTITION rx2015 VALUES LESS THAN( TO_DAYS('2015-01-01 00:00:00')) (SUBPARTITION subpart200, SUBPARTITION subpart201), 
PARTITION rx2016 VALUES LESS THAN( TO_DAYS('2016-01-01 00:00:00')) (SUBPARTITION subpart300, SUBPARTITION subpart301), 
PARTITION rxMORES VALUES LESS THAN (MAXVALUE) (SUBPARTITION subpartM00, SUBPARTITION subparM301));


CREATE TABLE Sub_Partitioned_test_from
(
Id Int,
	Title varchar(64),	
	Isin  varchar(16),	
	Country varchar(64),	
	Description varchar(128),	
	SecurityType varchar(16),
	Created date
) ENGINE=InnoDB DEFAULT CHARSET=latin1
PARTITION BY RANGE( TO_DAYS(Created) )
subpartition by hash (Id) (
PARTITION rx2014 VALUES LESS THAN( TO_DAYS('2014-01-01 00:00:00')) (SUBPARTITION subpart100, SUBPARTITION subpart101), 
PARTITION rx2015 VALUES LESS THAN( TO_DAYS('2015-01-01 00:00:00')) (SUBPARTITION subpart200, SUBPARTITION subpart201), 
PARTITION rx2016 VALUES LESS THAN( TO_DAYS('2016-01-01 00:00:00')) (SUBPARTITION subpart300, SUBPARTITION subpart301), 
PARTITION rxMORES VALUES LESS THAN (MAXVALUE) (SUBPARTITION subpartM00, SUBPARTITION subparM301));

insert into Sub_Partitioned_test_from values(1,'Intel Corp.',	'US4581401001',	'United States',	'Equity, ISIN US4581401001, WKN 855681, INL',	'Equity', now());
insert into Sub_Partitioned_test_from values(2,'INTEL.COMMUN.NEW DL-,0001',	'US45824F2048',	'United States',	'Equity, ISIN US45824F2048, WKN A1CSQX, B3CN',	'Equity', now());
insert into Sub_Partitioned_test_from values(3,'MICROSOFT 09/14',	'US594918AB00',	'United States',	'Bond, ISIN US594918AB00, WKN A0T922',	'Bond', now());
insert into Sub_Partitioned_test_from values(4,'MICROSOFT 09/19',	'US594918AC82',	'United States',	'Bond, ISIN US594918AC82, WKN A0T923',	'Bond', now());
insert into Sub_Partitioned_test_from values(5,'MICROSOFT 10/20',	'US594918AH79',	'United States',	'Bond, ISIN US594918AH79, WKN A1A1TC',	'Bond', now());
insert into Sub_Partitioned_test_from values(6,'IBM CORP. 08-11 MTN',	'CH0042308749',	'Switzerland',	'Bond, ISIN CH0042308749, WKN A0TVDX',	'Bond', now());
insert into Sub_Partitioned_test_from values(7,'IBM INTL GRP C. 2012',	'US44924EAB65',	'United States',	'Bond, ISIN US44924EAB65, WKN A0TLJY',	'Bond', now() );
insert into Sub_Partitioned_test_from values(8,'IBM CORP. 08-15 MTN',	'CH0042308780',	'Switzerland',	'Bond, ISIN CH0042308780, WKN A0TVEN',	'Bond', now() );
insert into Sub_Partitioned_test_from values(9,'Google Inc.',	'US38259P5089',	'US',	'Equity, ISIN US38259P5089, WKN A0B7FY, GGQ1',	'Equity', now() );
insert into Sub_Partitioned_test_from values(10,'Capped Bonus Zertifikat auf Google',	'DE000CM6F7G6'	,'Germany',	'Investment Product, ISIN DE000CM6F7G6, WKN CM6F7G',	'Investment',  now() );
insert into Sub_Partitioned_test_from values(11,'Capped Bonus Zertifikat auf Google',	'DE000CM6F7H4',	'Germany',	'Investment Product, ISIN DE000CM6F7H4, WKN CM6F7H',	'Investment', now() );
insert into Sub_Partitioned_test_from values(12,'FACEBOOK INC',	'US30303M1027',	'UNITED STATES OF AMERICA',	'SHS FACEBOOK INC ORD REG',	'EQUITY', now() );

insert into Sub_Partitioned_test_from values(13,'FACEBOOK INC',	'US30303M1027',	'UNITED STATES OF AMERICA',	'SHS FACEBOOK INC ORD BR',	'EQUITY', now() );
insert into Sub_Partitioned_test_from values(14,'STRUCT CERT 25/09/12(FACEBOOK)USD17.7584',	'GB00B82JJN65',	'Great Britain - GB',	'STRUCT CERT 25/09/12(FACEBOOK)USD17.7584',	'Certificat', now() );
insert into Sub_Partitioned_test_from values(15,'ORACLE 06/11',	'US68402LAE48',	'United States',	'Bond, ISIN US68402LAE48, WKN A0GUEX',	'Bond', now() );
insert into Sub_Partitioned_test_from values(16,'ORACLE 09/14',	'US68389XAF24',	'United States',	'Bond, ISIN US68389XAF24, WKN A1AJTX',	'Bond', now() );
insert into Sub_Partitioned_test_from values(17,'ORACLE 10/20 REGS',	'USU68308AA07',	'United States',	'Bond, ISIN USU68308AA07, WKN A1AY6N',	'Bond', now() );
insert into Sub_Partitioned_test_from values(18,'BANK OF AMERICA 2016',	'US638585AU38',	'United States',	'Bond, ISIN US638585AU38, WKN 829067',	'Bond', now() );
insert into Sub_Partitioned_test_from values(19,'BANK OF AMERICA 2028',	'US338915AH41',	'United States',	'Bond, ISIN US338915AH41, WKN 355410',	'Bond', now() );

insert into Sub_Partitioned_test_from values(20,'BANK OF AMERICA 2028',	'US338915AM36',	'United States',	'Bond, ISIN US338915AM36, WKN 155239',	'Bond', now() );
insert into Sub_Partitioned_test_from values(21,'MORGAN STANLEY 02/12MTN',	'US617446HC69',	'United States',	'Bond, ISIN US617446HC69, WKN 853722',	'Bond',now() );
insert into Sub_Partitioned_test_from values(22,'MORGAN STANLEY 02/32MTN',	'US617446HD43',	'United States',	'Bond, ISIN US617446HD43, WKN 853723',	'Bond',now() );
insert into Sub_Partitioned_test_from values(23,'MORGAN STANLEY 03/13MTN',	'US617446HS12',	'United States',	'Bond, ISIN US617446HS12, WKN 776381',	'Bond', now() );
insert into Sub_Partitioned_test_from values(24,'CITIBANK N.A. 09/12',	'US17290CAB28',	'United States',	'Bond, ISIN US17290CAB28, WKN A1AHUG',	'Bond',now() );
insert into Sub_Partitioned_test_from values(25,'CITIBANK N.A. 2011',	'US17314JAN37',	'United States',	'Bond, ISIN US17314JAN37, WKN A1AK2M',	'Bond',now() );
insert into Sub_Partitioned_test_from values(26,'CITIBANK N.A. 2012',	'US17314JAT07',	'United States',	'Bond, ISIN US17314JAT07, WKN A1AN8G',	'Bond', now() );

insert into Sub_Partitioned_test_from values(27,'COMCAST CAB.COM.HLD.02/13',	'US00209TAA34',	'United States',	'Bond, ISIN US00209TAA34, WKN 214099',	'Bond', now() );
insert into Sub_Partitioned_test_from values(28,'COMCAST NEW 06/17',	'US20030NAP69',	'United States',	'Bond, ISIN US20030NAP69, WKN A0GVTR',	'Bond', now() );
insert into Sub_Partitioned_test_from values(29,'COMCAST NEW 07/17',	'US20030NAU54',	'United States',	'Bond, ISIN US20030NAU54, WKN A0N11L',	'Bond',now() );
insert into Sub_Partitioned_test_from values(30,'TRUVO SUBS. 04/14 REGS',	'XS0206614702',	'XS',	'Bond, ISIN XS0206614702, WKN A0DHDH',	'Bond',now() );
insert into Sub_Partitioned_test_from values(31,'UBS (LUXEMB.) 06/16 REGS',	'XS0253861834',	'XS',	'Bond, ISIN XS0253861834, WKN A0GSAR',	'Bond',now() );
insert into Sub_Partitioned_test_from values(32,'UBS (STAMFORD BR.) 10/12',	'US90261XGA46',	'United States',	'Bond, ISIN US90261XGA46, WKN A1AT4G',	'Bond', now() );
insert into Sub_Partitioned_test_from values(33,'Deutsche Bank AG',	'DE0005140008',	'Germany',	'Equity, ISIN DE0005140008, WKN 514000, DBK',	'Equity',now() );

insert into Sub_Partitioned_test_from values(34,'Aktien-Anleihe auf Deutsche Bank',	'DE000BLB8CL7',	'Germany',	'Investment Product, ISIN DE000BLB8CL7, WKN BLB8CL',	'Investment', now() );
insert into Sub_Partitioned_test_from values(35,'Bonus-Zertifikat auf Deutsche Bank',	'DE000SG1ZT01',	'Germany',	'Investment Product, ISIN DE000SG1ZT01, WKN SG1ZT0',	'Investment', now() );
insert into Sub_Partitioned_test_from values(36,'YAHOO JAPAN CORP.',	'JP3933800009',	'Japan',	'Equity, ISIN JP3933800009, WKN 916008, YOJ',	'Equity', now() );
insert into Sub_Partitioned_test_from values(37,'Yahoo! Inc.',	'US9843321061',	'United States',	'Equity, ISIN US9843321061, WKN 900103, YHO',	'Equity', now() );
insert into Sub_Partitioned_test_from values(38,'Discountzertifikat Classic auf Yahoo',	'DE000CM7YZ34',	'Germany',	'Investment Product, ISIN DE000CM7YZ34, WKN CM7YZ3',	'Investment', now() );
insert into Sub_Partitioned_test_from values(39,'Allianz PIMCO Bondselect US $ - AT - USD',	'LU0035450757',	'Luxembourg',	'Funds, ISIN LU0035450757, WKN 971769, AZHL',	'Fund', now() );
insert into Sub_Partitioned_test_from values(40,'Allianz PIMCO Bondspezial - A - EUR',	'LU0006245863',	'Luxembourg',	'Funds, ISIN LU0006245863, WKN 971114, DJED',	'Fund', now() );
insert into Sub_Partitioned_test_from values(41,'Allianz PIMCO Convertible Bonds P',	'DE000A0ND6L9',	'Germany',	'Funds, ISIN DE000A0ND6L9, WKN A0ND6L, LQ6Q',	'Fund', now() );
insert into Sub_Partitioned_test_from values(42,'CITCO TRUSTEES (CAYMAN) LIMITED',	'US17302TAA34',	'CAYMAN ISLANDS',	'USD 8,50 CITGO TRUSTEES CAYMAN(144A)04-2014',	'DEBT', now() );
insert into Sub_Partitioned_test_from values(43,'CITCO TRUSTEES (CAYMAN) LIMITED',	'USG2149YAA40',	'CAYMAN ISLANDS',	'USD 8,50 CITGO TR. CAYMAN (REGS) 04-2014',	'DEBT', now() );



