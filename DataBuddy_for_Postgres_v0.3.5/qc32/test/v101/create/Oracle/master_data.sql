create table master_data (
	Title varchar2(64),	
	Isin  varchar2(16),	
	Country varchar2(64),	
	Description varchar2(128),	
	SecurityType varchar2(16),
	Created date, 
	modified timestamp, 
	retired TIMESTAMP WITH TIME ZONE);
	
insert into master_data values('IBM CORP. 08-11 MTN',	'CH0042308749',	'Switzerland',	'Bond, ISIN CH0042308749, WKN A0TVDX',	'Bond', trunc(sysdate), SYSTIMESTAMP , SYSTIMESTAMP );
insert into master_data values('IBM INTL GRP C. 2012',	'US44924EAB65',	'United States',	'Bond, ISIN US44924EAB65, WKN A0TLJY',	'Bond',trunc(sysdate), SYSTIMESTAMP , SYSTIMESTAMP );
insert into master_data values('IBM CORP. 08-15 MTN',	'CH0042308780',	'Switzerland',	'Bond, ISIN CH0042308780, WKN A0TVEN',	'Bond', trunc(sysdate), SYSTIMESTAMP , SYSTIMESTAMP );
insert into master_data values('Google Inc.',	'US38259P5089',	'US',	'Equity, ISIN US38259P5089, WKN A0B7FY, GGQ1',	'Equity',trunc(sysdate), SYSTIMESTAMP , SYSTIMESTAMP );
insert into master_data values('Capped Bonus Zertifikat auf Google',	'DE000CM6F7G6'	,'Germany',	'Investment Product, ISIN DE000CM6F7G6, WKN CM6F7G',	'Investment',trunc(sysdate), SYSTIMESTAMP , SYSTIMESTAMP );
insert into master_data values('Capped Bonus Zertifikat auf Google',	'DE000CM6F7H4',	'Germany',	'Investment Product, ISIN DE000CM6F7H4, WKN CM6F7H',	'Investment',trunc(sysdate), SYSTIMESTAMP , SYSTIMESTAMP );
insert into master_data values('FACEBOOK INC',	'US30303M1027',	'UNITED STATES OF AMERICA',	'SHS FACEBOOK INC ORD REG',	'EQUITY',trunc(sysdate), SYSTIMESTAMP , SYSTIMESTAMP );
insert into master_data values('FACEBOOK INC',	'US30303M1027',	'UNITED STATES OF AMERICA',	'SHS FACEBOOK INC ORD BR',	'EQUITY',trunc(sysdate), SYSTIMESTAMP , SYSTIMESTAMP );
insert into master_data values('STRUCT CERT 25/09/12(FACEBOOK)USD17.7584',	'GB00B82JJN65',	'Great Britain - GB',	'STRUCT CERT 25/09/12(FACEBOOK)USD17.7584',	'Certificat',trunc(sysdate), SYSTIMESTAMP , SYSTIMESTAMP );
insert into master_data values('ORACLE 06/11',	'US68402LAE48',	'United States',	'Bond, ISIN US68402LAE48, WKN A0GUEX',	'Bond',trunc(sysdate), SYSTIMESTAMP , SYSTIMESTAMP );
insert into master_data values('ORACLE 09/14',	'US68389XAF24',	'United States',	'Bond, ISIN US68389XAF24, WKN A1AJTX',	'Bond',trunc(sysdate), SYSTIMESTAMP , SYSTIMESTAMP );
insert into master_data values('ORACLE 10/20 REGS',	'USU68308AA07',	'United States',	'Bond, ISIN USU68308AA07, WKN A1AY6N',	'Bond',trunc(sysdate), SYSTIMESTAMP , SYSTIMESTAMP );
insert into master_data values('BANK OF AMERICA 2016',	'US638585AU38',	'United States',	'Bond, ISIN US638585AU38, WKN 829067',	'Bond',trunc(sysdate), SYSTIMESTAMP , SYSTIMESTAMP );
insert into master_data values('BANK OF AMERICA 2028',	'US338915AH41',	'United States',	'Bond, ISIN US338915AH41, WKN 355410',	'Bond',trunc(sysdate), SYSTIMESTAMP , SYSTIMESTAMP );
insert into master_data values('BANK OF AMERICA 2028',	'US338915AM36',	'United States',	'Bond, ISIN US338915AM36, WKN 155239',	'Bond',trunc(sysdate), SYSTIMESTAMP , SYSTIMESTAMP );
insert into master_data values('MORGAN STANLEY 02/12MTN',	'US617446HC69',	'United States',	'Bond, ISIN US617446HC69, WKN 853722',	'Bond',trunc(sysdate), SYSTIMESTAMP , SYSTIMESTAMP );
insert into master_data values('MORGAN STANLEY 02/32MTN',	'US617446HD43',	'United States',	'Bond, ISIN US617446HD43, WKN 853723',	'Bond',trunc(sysdate), SYSTIMESTAMP , SYSTIMESTAMP );
insert into master_data values('MORGAN STANLEY 03/13MTN',	'US617446HS12',	'United States',	'Bond, ISIN US617446HS12, WKN 776381',	'Bond',trunc(sysdate), SYSTIMESTAMP , SYSTIMESTAMP );
insert into master_data values('CITIBANK N.A. 09/12',	'US17290CAB28',	'United States',	'Bond, ISIN US17290CAB28, WKN A1AHUG',	'Bond',trunc(sysdate), SYSTIMESTAMP , SYSTIMESTAMP );
insert into master_data values('CITIBANK N.A. 2011',	'US17314JAN37',	'United States',	'Bond, ISIN US17314JAN37, WKN A1AK2M',	'Bond',trunc(sysdate), SYSTIMESTAMP , SYSTIMESTAMP );
insert into master_data values('CITIBANK N.A. 2012',	'US17314JAT07',	'United States',	'Bond, ISIN US17314JAT07, WKN A1AN8G',	'Bond',trunc(sysdate), SYSTIMESTAMP , SYSTIMESTAMP );
insert into master_data values('COMCAST CAB.COM.HLD.02/13',	'US00209TAA34',	'United States',	'Bond, ISIN US00209TAA34, WKN 214099',	'Bond',trunc(sysdate), SYSTIMESTAMP , SYSTIMESTAMP );
insert into master_data values('COMCAST NEW 06/17',	'US20030NAP69',	'United States',	'Bond, ISIN US20030NAP69, WKN A0GVTR',	'Bond',trunc(sysdate), SYSTIMESTAMP , SYSTIMESTAMP );
insert into master_data values('COMCAST NEW 07/17',	'US20030NAU54',	'United States',	'Bond, ISIN US20030NAU54, WKN A0N11L',	'Bond',trunc(sysdate), SYSTIMESTAMP , SYSTIMESTAMP );
insert into master_data values('TRUVO SUBS. 04/14 REGS',	'XS0206614702',	'XS',	'Bond, ISIN XS0206614702, WKN A0DHDH',	'Bond',trunc(sysdate), SYSTIMESTAMP , SYSTIMESTAMP );
insert into master_data values('UBS (LUXEMB.) 06/16 REGS',	'XS0253861834',	'XS',	'Bond, ISIN XS0253861834, WKN A0GSAR',	'Bond',trunc(sysdate), SYSTIMESTAMP , SYSTIMESTAMP );
insert into master_data values('UBS (STAMFORD BR.) 10/12',	'US90261XGA46',	'United States',	'Bond, ISIN US90261XGA46, WKN A1AT4G',	'Bond',trunc(sysdate), SYSTIMESTAMP , SYSTIMESTAMP );
insert into master_data values('Deutsche Bank AG',	'DE0005140008',	'Germany',	'Equity, ISIN DE0005140008, WKN 514000, DBK',	'Equity',trunc(sysdate), SYSTIMESTAMP , SYSTIMESTAMP );
insert into master_data values('Aktien-Anleihe auf Deutsche Bank',	'DE000BLB8CL7',	'Germany',	'Investment Product, ISIN DE000BLB8CL7, WKN BLB8CL',	'Investment',trunc(sysdate), SYSTIMESTAMP , SYSTIMESTAMP );
insert into master_data values('Bonus-Zertifikat auf Deutsche Bank',	'DE000SG1ZT01',	'Germany',	'Investment Product, ISIN DE000SG1ZT01, WKN SG1ZT0',	'Investment',trunc(sysdate), SYSTIMESTAMP , SYSTIMESTAMP );
insert into master_data values('YAHOO JAPAN CORP.',	'JP3933800009',	'Japan',	'Equity, ISIN JP3933800009, WKN 916008, YOJ',	'Equity',trunc(sysdate), SYSTIMESTAMP , SYSTIMESTAMP );
insert into master_data values('Yahoo! Inc.',	'US9843321061',	'United States',	'Equity, ISIN US9843321061, WKN 900103, YHO',	'Equity',trunc(sysdate), SYSTIMESTAMP , SYSTIMESTAMP );
insert into master_data values('Discountzertifikat Classic auf Yahoo',	'DE000CM7YZ34',	'Germany',	'Investment Product, ISIN DE000CM7YZ34, WKN CM7YZ3',	'Investment',trunc(sysdate), SYSTIMESTAMP , SYSTIMESTAMP );
insert into master_data values('Allianz PIMCO Bondselect US $ - AT - USD',	'LU0035450757',	'Luxembourg',	'Funds, ISIN LU0035450757, WKN 971769, AZHL',	'Fund',trunc(sysdate), SYSTIMESTAMP , SYSTIMESTAMP );
insert into master_data values('Allianz PIMCO Bondspezial - A - EUR',	'LU0006245863',	'Luxembourg',	'Funds, ISIN LU0006245863, WKN 971114, DJED',	'Fund',trunc(sysdate), SYSTIMESTAMP , SYSTIMESTAMP );
insert into master_data values('Allianz PIMCO Convertible Bonds P',	'DE000A0ND6L9',	'Germany',	'Funds, ISIN DE000A0ND6L9, WKN A0ND6L, LQ6Q',	'Fund',trunc(sysdate), SYSTIMESTAMP , SYSTIMESTAMP );
insert into master_data values('CITCO TRUSTEES (CAYMAN) LIMITED',	'US17302TAA34',	'CAYMAN ISLANDS',	'USD 8,50 CITGO TRUSTEES CAYMAN(144A)04-2014',	'DEBT',trunc(sysdate), SYSTIMESTAMP , SYSTIMESTAMP );
insert into master_data values('CITCO TRUSTEES (CAYMAN) LIMITED',	'USG2149YAA40',	'CAYMAN ISLANDS',	'USD 8,50 CITGO TR. CAYMAN (REGS) 04-2014',	'DEBT',trunc(sysdate), SYSTIMESTAMP , SYSTIMESTAMP );
