CREATE DATABASE IF NOT EXISTS GroceryTech /*!40100 DEFAULT CHARACTER SET latin1 */;
use GroceryTech;

--
-- Fresh initialization of the database
--
DROP TABLE IF EXISTS `SystemInformation`;
DROP TABLE IF EXISTS `Payments`;
DROP TABLE IF EXISTS `manages`;
DROP TABLE IF EXISTS `orderedBy`;
DROP TABLE IF EXISTS `selectItem`;
DROP TABLE IF EXISTS `orderFrom`;
DROP TABLE IF EXISTS `soldAt`;
DROP TABLE IF EXISTS `deliveredBy`;
DROP TABLE IF EXISTS `Buyer`;
DROP TABLE IF EXISTS `Item`;
DROP TABLE IF EXISTS `Orderr`;
DROP TABLE IF EXISTS `GroceryStore`;
DROP TABLE IF EXISTS `Address`;
DROP TABLE IF EXISTS `Userr`;



--
-- Table structure for table `SystemInformation`
--
CREATE TABLE SystemInformation ( 
    system_id             INT (2)        NOT NULL,
    user_codes             INT(16)        NOT NULL,
    PRIMARY KEY (system_id)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `SystemInformation`
--

LOCK TABLES `SystemInformation` WRITE; 
INSERT INTO `SystemInformation` VALUES (0, 123456789), (1, 777888999);
UNLOCK TABLES;



--
-- Table structure for table `Address`
--
CREATE TABLE Address (
    id                INT(2)            NOT NULL,
house_number            INT(8)            NOT NULL,
street                VARCHAR(64)        NOT NULL,
    city                VARCHAR(16)        NOT NULL,
state                VARCHAR(16)        NOT NULL,
    zip_code            INT(8)            NOT NULL,
    PRIMARY KEY (id)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `Address`
--

LOCK TABLES `Address` WRITE; 
INSERT INTO `Address` VALUES (1, 9093, 'Dorrit Crescent', 'Atlanta', 'Georgia', 30312), (2, 1438, 'White Horse Piece', 'Atlanta', 'Georgia', 30312), (3, 6823, 'Bornedene', 'Atlanta', 'Georgia', 30312), (4, 9550, 'Ramsey Side', 'Atlanta', 'Georgia', 30312), (5, 8669, 'Hare Pines', 'Atlanta', 'Georgia', 30312), (6, 8001, 'Peggieshill Road', 'Atlanta', 'Georgia', 30312), (7, 9493, 'Langdale Copse', 'Atlanta', 'Georgia', 30312), (8, 3093, 'Albion Wynd', 'Atlanta', 'Georgia', 30312), (9, 3984, 'Linnet Mill', 'Atlanta', 'Georgia', 30312), (10, 6968, 'Elgar Limes', 'Atlanta', 'Georgia', 30312), (11, 6521, 'Moor Hill Road', 'Atlanta', 'Georgia', 30312), (12, 1431, "St James's Drove", 'Atlanta', 'Georgia', 30322), (13, 4163, 'Chequers Leas', 'Atlanta', 'Georgia', 30322), (14, 968, 'Canterbury Way', 'Atlanta', 'Georgia', 30322), (15, 2427, 'Moss Rowans', 'Atlanta', 'Georgia', 30322), (16, 6024, 'Allan Side', 'Atlanta', 'Georgia', 30322), (17, 2210, 'Fleet Leaze', 'Atlanta', 'Georgia', 30322), (18, 5563, 'Mill Hill Street', 'Atlanta', 'Georgia', 31873), (19, 1112, 'Grampian Down', 'Atlanta', 'Georgia', 31873), (20, 4688, 'East Central Drive', 'Atlanta', 'Georgia', 31873), (21, 6537, 'Bessbrook Road', 'Atlanta', 'Georgia', 31873), (22, 2616, 'Recreation Pines', 'Atlanta', 'Georgia', 31873), (23, 6873, 'Fifth Manor', 'Decatur', 'Georgia', 33090), (24, 6696, 'Post Office Willows', 'Decatur', 'Georgia', 33090), (25, 8961, 'Kennedy Firs', 'Decatur', 'Georgia', 33090), (26, 5556, 'Selby Ride', 'Decatur', 'Georgia', 33090), (27, 7898, 'Melland Road', 'Decatur', 'Georgia', 33090), (28, 2245, 'Causeway By-Pass', 'Marietta', 'Georgia', 38899), (29, 3518, 'Maesteg Terrace', 'Marietta', 'Georgia', 38899), (30, 5037, 'Browns Drive', 'Marietta', 'Georgia', 38899), (31, 1294, 'Bells Wood Court', 'Marietta', 'Georgia', 34999), (32, 8526, 'Sandringham Banks', 'Marietta', 'Georgia', 31111), (33, 7971, 'Anglesey Drift', 'Atlanta', 'Georgia', 30312), (34, 7912, 'Crown Terrace', 'Atlanta', 'Georgia', 30312), (35, 6491, 'Valley Corner', 'Atlanta', 'Georgia', 30312), (36, 5728, 'Southgate Royd', 'Atlanta', 'Georgia', 30312), (37, 2445, 'Garnlwyd Close', 'Atlanta', 'Georgia', 30312), (38, 1758, 'Hyde Grove', 'Atlanta', 'Georgia', 30312), (39, 8754, 'Brewery Oval', 'Atlanta', 'Georgia', 30312), (40, 6745, 'Archer Laurels', 'Atlanta', 'Georgia', 30312), (41, 6158, 'West View Village', 'Atlanta', 'Georgia', 30312), (42, 3758, 'Barley Brae', 'Atlanta', 'Georgia', 30312), (43, 6161, 'Belvedere Cottages', 'Atlanta', 'Georgia', 30312), (44, 1105, 'Lark Leas', 'Atlanta', 'Georgia', 30322), (45, 5165, 'Belton Hey', 'Atlanta', 'Georgia', 30322), (46, 1554, 'Adam Corner', 'Atlanta', 'Georgia', 30322), (47, 9097, 'Fisher Brook', 'Atlanta', 'Georgia', 30322), (48, 384, 'Andover Hollies', 'Atlanta', 'Georgia', 30322), (49, 378, 'Grant Brow', 'Atlanta', 'Georgia', 30322), (50, 4716, 'Warrington Newydd', 'Atlanta', 'Georgia', 31873), (51, 2618, 'Silverdale Wharf', 'Atlanta', 'Georgia', 31873), (52, 3424, 'Backsands Lane', 'Atlanta', 'Georgia', 31873), (53, 8505, 'Netherfield Dene', 'Atlanta', 'Georgia', 31873), (54, 7158, 'Windings Road', 'Atlanta', 'Georgia', 31873), (55, 1338, 'Byker Street', 'Decatur', 'Georgia', 33090), (56, 8134, 'Anglesey Ride', 'Decatur', 'Georgia', 33090), (57, 4769, 'Moorlands Leaze', 'Decatur', 'Georgia', 33090), (58, 782, 'Gipton Gate East', 'Decatur', 'Georgia', 33090), (59, 6953, 'Marina Paddocks', 'Decatur', 'Georgia', 33090), (60, 9923, 'Brackley Drove', 'Marietta', 'Georgia', 38899), (61, 4933, 'Godbold Road', 'Marietta', 'Georgia', 38899), (62, 1203, 'Frogmire Close', 'Marietta', 'Georgia', 38899), (63, 742, 'Vaughan Pines', 'Marietta', 'Georgia', 34999), (64, 8261, 'Parkside East', 'Marietta', 'Georgia', 31111), (65, 8328, 'Montpelier Newydd', 'Atlanta', 'Georgia', 30312), (66, 8897, 'Bell Weir Close', 'Atlanta', 'Georgia', 30312), (67, 4490, 'Fourth Field', 'Atlanta', 'Georgia', 30312);
UNLOCK TABLES;




--
-- Table structure for table `Userr`
--
CREATE TABLE Userr ( 
    username            VARCHAR(64)        NOT NULL,
    password            VARCHAR(64)        NOT NULL,
    user_type            VARCHAR(16)        NOT NULL,
email                VARCHAR(64)        NOT NULL,
first_name            VARCHAR(16)        NOT NULL,
    last_name            VARCHAR(16)        NOT NULL,
    PRIMARY KEY(username) 
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `Userr`
--

LOCK TABLES `Userr` WRITE; 
INSERT INTO `Userr` VALUES ('adepttimberry', 'cakeholmium', 'buyer', 'dingconie@gmail.com', 'Ganizani', 'States'), ('admirableneville', 'apricotsscandium', 'buyer', 'fripperychamois@yahoo.com', 'Wolfgang', 'Stranberg'), ('bossywilfer', 'bagelsantimony', 'buyer', 'magmacoyote@comcast.net', 'Fintan', 'Lewis'), ('bowedhannibal', 'polentahafnium', 'buyer', 'rhubarbcheetah@gatech.edu', 'Tempest', 'Donnerstein'), ('breakabletim', 'milkshakestin', 'buyer', 'manholeiguana@gmail.com', 'Nakato', 'Matlock'), ('coldsnewkes', 'oilstrontium', 'buyer', 'lozengecattle@gatech.edu', 'Eurydike', 'Saar'), ('corruptbayton', 'garliccerium', 'buyer', 'crudivorebarracuda@gmail.com', 'Joonas', 'Larkin'), ('dazzlingjohnny', 'doughnutaluminum', 'buyer', 'rickshawtoucan@gmail.com', 'Elmas', 'Davenport'), ('decimalherbert', 'riceuranium', 'buyer', 'bloviatecardinal@yahoo.com', 'Sawyer', 'Baltz'), ('disfiguredalderman', 'chileerbium', 'buyer', 'flannelcurlew@yahoo.com', 'Rajendra', 'Wicks'), ('fainthannah', 'oatmealgold', 'buyer', 'fardsandpiper@gmail.com', 'Petronela', 'Kelvin'), ('firmdedlock', 'lardpalladium', 'buyer', 'poppysmicgoose@gmail.com', 'Bilyana', 'Cuthbertson'), ('freshpeltirogus', 'caviardubnium', 'buyer', 'gashbaboon@yahoo.com', 'Haig', 'Heyde'), ('frightenedsmallweed', 'mueslicurium', 'buyer', 'bamboodingo@gmail.com', 'Hannibal', 'Engell'), ('hurriedplornish', 'coconutcopper', 'buyer', 'doodlepolarbear@yahoo.com', 'Maximilien', 'Felix'), ('inactivejane', 'pepperoniberyllium', 'buyer', 'snarkypeafowl@comcast.net', 'Nelli', 'Dimare'), ('maddeningfladdock', 'abaloneterbium', 'buyer', 'smashinggoldfinch@gmail.com', 'Nadja', 'Fienberg'), ('marvelousjinkins', 'pistachiopraseodymium', 'buyer', 'drizzlebacteria@comcast.net', 'Anneliese', 'Dickson'), ('melodicsparkler', 'raisinsthorium', 'buyer', 'wabbitkapi@gmail.com', 'Vera', 'Agee'), ('noxiousmould', 'trufflemanganese', 'buyer', 'codswallopbobolink@gmail.com', 'Shui', 'Agostinelli'), ('putridsnagsby', 'gatoradecalifornium', 'buyer', 'liripoopunicorn@gatech.edu', 'Jupiter', 'Leitman'), ('rowdysteerforth', 'crackersosmium', 'buyer', 'sickleturtle@gmail.com', 'Mahesh', 'Parsons'), ('sablemagnus', 'sausageastatine', 'buyer', 'lugubriousquail@gmail.com', 'Lauma', 'Romberger'), ('severelucy', 'burritosneptunium', 'buyer', 'cougarcur@gmail.com', 'Brendan', 'Pool'), ('snobbymorleena', 'granolaniobium', 'buyer', 'nincompoopcockatoo@gmail.com', 'Hieremihel', 'Doeringer'), ('tastyadams', 'puddingneon', 'buyer', 'crunchcapon@gmail.com', 'Sextilius', 'Blew'), ('torpidkenge', 'syrupsilicon', 'buyer', 'dollopcoot@comcast.net', 'Pravin', 'Blumberg'), ('unwrittensloppy', 'tacoseuropium', 'buyer', 'felinerat@gmail.com', 'Evalds', 'Carper'), ('vitalbetty', 'pepperthallium', 'buyer', 'centipedeanaconda@gmail.com', 'Agneta', 'Inoue'), ('welcomeleicester', 'cheeseboron', 'buyer', 'igloopilchard@gmail.com', 'Moric', 'Prezelin'), ('wellmadeconkey', 'cordialsamarium', 'buyer', 'chinchillapanda@gmail.com', 'Feliciana', 'Burgio'), ('woozyprice', 'venisonlithium', 'buyer', 'snoutoxbird@gmail.com', 'Lelia', 'Marschall'), ('chivalrouspotatoes', 'clamcarbon', 'deliverer', 'pratfallwhiting@gmail.com', 'Clio', 'Allitto'), ('downrightcorney', 'basmatiphosphorus', 'deliverer', 'pantsdunlin@gmail.com', 'Katerina', 'Rowse'), ('glumsmike', 'salamiiridium', 'deliverer', 'folderolraccoon@yahoo.com', 'Nimet', 'Bogorad'), ('inventivenickleby', 'sardinesoxygen', 'deliverer', 'gazebolinnet@comcast.net', 'Greta', 'Berkowitz'), ('languidtopsawyer', 'applestitanium', 'deliverer', 'conniptionbadger@gatech.edu', 'Rivka', 'Guenthart'), ('methodicalcharity', 'pearfrancium', 'deliverer', 'glomhound@comcast.net', 'Alessio', 'Griesenbeck'), ('reasonablewrayburn', 'saltradium', 'deliverer', 'glabellaswift@yahoo.com', 'Hamida', 'Gugel'), ('shadowywestlock', 'orangetellurium', 'deliverer', 'samovartuna@gmail.com', 'Hristijan', 'Furshpan'), ('spiffyjudith', 'eggsselenium', 'deliverer', 'fuddyduddyvole@gmail.com', 'Aerona', 'Agren'), ('stylishtowlinson', 'jerkygermanium', 'deliverer', 'masticateguillemot@gmail.com', 'Breixo', 'Sanders'), ('teenyroads', 'icecreamargon', 'deliverer', 'goonavocet@gmail.com', 'Matty', 'Von kapff'), ('twinchicken', 'vegetablesprotactinium', 'deliverer', 'bobbintamarin@comcast.net', 'Riannon', 'Kelsch'), ('unknownswidger', 'tomatoeplutonium', 'deliverer', 'filibusterbuck@comcast.net', 'Oto', 'Bayo'), ('colorlessabbey', 'mayonnaisemeitnerium', 'manager', 'noodleschimpanzee@gmail.com', 'Blythe', 'Aiken'), ('optimalpluck', 'quicheiron', 'manager', 'sousaphonegnu@yahoo.com', 'Doris', 'Bae'), ('quickestmortimer', 'lolliescalcium', 'manager', 'allegatorhornet@gatech.edu', 'Tarana', 'Goodwin'), ('smoothbetsy', 'paellatechnetium', 'manager', 'shenaniganbison@gatech.edu', 'Hilde', 'Secor'), ('pepsisilicon', 'hondapromethium', 'manager', 'pepsisilicon@gmail.com', 'Aime', 'Stephenson'), ('facebookoxygen', 'chaseiodine', 'manager', 'facebookoxygen@comcast.net', 'Tiburcio', 'Lans'), ('hyundaimeitnerium', 'ferrariberkelium', 'manager', 'hyundaimeitnerium@gmail.com', 'Katri', 'Lehr'), ('colgatesulfur', 'volkswagonholmium', 'manager', 'colgatesulfur@gmail.com', 'Benedict', 'Reinhardt'), ('mcdonaldssodium', 'shelltitanium', 'manager', 'mcdonaldssodium@gatech.edu', 'Lorayne', 'Bretscher'), ('amazonzirconium', 'dellyttrium', 'manager', 'amazonzirconium@gatech.edu', 'Bartholomei', 'Holm'), ('nescafeselenium', 'applechlorine', 'manager', 'nescafeselenium@comcast.net', 'Melqart', 'Voligny'), ('chaneliridium', 'microsoftactinium', 'manager', 'chaneliridium@gatech.edu', 'Dragos', 'Shephard'), ('heinzrutherfordium', 'allianztin', 'manager', 'heinzrutherfordium@gmail.com', 'Kynthia', 'Ramella'), ('visahafnium', 'audihassium', 'manager', 'visahafnium@gmail.com', 'Klara', 'Meehan'), ('chevroletberyllium', 'kellogsterbium', 'manager', 'chevroletberyllium@gatech.edu', 'Adrian', 'Chayes'), ('guccinickel', 'krafthydrogen', 'manager', 'guccinickel@gmail.com', 'Nyoman', 'Mccue'), ('exxonindium', 'cartiercalifornium', 'manager', 'exxonindium@gmail.com', 'Wairimu', 'Wiske'), ('pradaphosphorus', 'nestlemercury', 'manager', 'pradaphosphorus@comcast.net', 'Henrikas', 'Stine'), ('ciscocobalt', 'santandercesium', 'manager', 'ciscocobalt@gmail.com', 'Manuela', 'Saivetz'), ('lancomegermanium', 'siemenschromium', 'manager', 'lancomegermanium@gmail.com', 'Tobiah', 'Currall'), ('foxbarium', 'colauranium', 'manager', 'foxbarium@gmail.com', 'Ernust', 'Nupdal'), ('starbucksrhenium', 'pampersfermium', 'manager', 'starbucksrhenium@gatech.edu', 'Sybella', 'Stagliano'), ('adidaslawrencium', 'ibmpalladium', 'manager', 'adidaslawrencium@comcast.net', 'Alberich', 'Fauroat'), ('heinekenplatinum', 'toyotasilicon', 'manager', 'heinekenplatinum@gmail.com', 'Lorinda', 'Kinlin'), ('rolexfluorine', 'ciscorhodium', 'manager', 'rolexfluorine@comcast.net', 'Wallace', 'Castelda'), ('toyotacarbon', 'colayttrium', 'manager', 'toyotacarbon@comcast.net', 'Kathe', 'Forte'), ('gillettetellurium', 'santandercalifornium', 'manager', 'gillettetellurium@comcast.net', 'Branca', 'Schroth'), ('lexuslanthanum', 'philipslutetium', 'manager', 'lexuslanthanum@gmail.com', 'Alte', 'Renner'), ('boeingaluminum', 'nescafeiodine', 'manager', 'boeingaluminum@gmail.com', 'Niga', 'Sacchetti'), ('fordlead', 'nissanindium', 'manager', 'fordlead@gmail.com', 'Geronimo', 'Sobol'), ('canonxenon', 'ikearadium', 'manager', 'canonxenon@gatech.edu', 'Duri', 'Glazer'), ('burberrycopper', 'guccihydrogen', 'manager', 'burberrycopper@gmail.com', 'Nereus', 'Kearns'), ('malboroneodymium', 'foxsulfur', 'manager', 'malboroneodymium@gmail.com', 'Mari', 'Medin'), ('legothorium', 'gillettecerium', 'manager', 'legothorium@gmail.com', 'Anselm', 'Parnas'), ('batmanisbetterthanmoonknight', 'duhduhduh', 'manager', 'batmanisbetterthanmoonknight@ofcourse.yeah', 'Bruce', 'Campbell');
UNLOCK TABLES;




--
-- Table structure for table `GroceryStore`
--
CREATE TABLE GroceryStore (
    store_id              INT(2)             NOT NULL,
    store_name            VARCHAR(16)        NOT NULL,
    address_id            INT(2)            NOT NULL,
    opening_time            TIME            NOT NULL,
    closing_time            TIME            NOT NULL,
    phone                CHAR(16)        NOT NULL,
    PRIMARY KEY (store_id),
    CONSTRAINT ad9 FOREIGN KEY(address_id) REFERENCES Address (id) ON DELETE CASCADE ON UPDATE CASCADE   
) ENGINE=InnoDB DEFAULT CHARSET=latin1;


--
-- Dumping data for table `GroceryStore`
--

LOCK TABLES `GroceryStore` WRITE; 
INSERT INTO `GroceryStore` VALUES (1, 'Publix ', 33, '06:00', '05:20', 6445119852), (2, 'Publix ', 34, '06:05', '06:05', 5793205609), (3, 'Publix ', 35, '06:20', '06:15', 2256640936), (4, 'Publix ', 36, '06:45', '07:15', 7972476937), (5, 'Publix ', 37, '07:40', '07:35', 6028201944), (6, 'Publix ', 38, '08:00', '08:05', 9099566005), (7, 'Publix ', 39, '08:10', '08:45', 3674680760), (8, 'Kroger', 40, '08:15', '09:10', 6673099641), (9, 'Kroger', 41, '08:50', '09:20', 9873883807), (10, 'Kroger', 42, '08:55', '09:50', 5978516107), (11, 'Kroger', 43, '09:05', '11:05', 9953513489), (12, 'Kroger', 44, '09:40', '11:15', 3987590108), (13, 'Kroger', 45, '09:50', '11:20', 9598997019), (14, 'Whole Foods', 46, '10:25', '11:25', 4174612109), (15, 'Whole Foods', 47, '10:30', '11:30', 7568563917), (16, 'Sprouts', 48, '10:35', '11:40', 5526840452), (17, 'Sprouts', 49, '11:05', '11:45', 2992324086), (18, 'Piggly Wiggly', 50, '11:50', '12:10', 4227524132), (19, 'Walmart', 51, '12:00', '12:35', 6447655890), (20, 'Walmart', 52, '12:10', '13:55', 4722211749), (21, 'Target', 53, '12:40', '14:00', 2215141847), (22, 'Target', 54, '12:45', '14:05', 6038604265), (23, 'Aldi', 55, '14:25', '14:25', 5944719741), (24, 'Aldi', 56, '14:50', '15:45', 3214372158), (25, 'Aldi', 57, '15:10', '16:05', 4584491073), (26, 'Winndixie', 58, '15:15', '16:15', 8288693331), (27, 'Sams', 59, '17:00', '17:35', 8466490485), (28, 'Sams', 60, '17:30', '17:50', 2678220931), (29, 'Sams', 61, '18:10', '18:00', 4135804574), (30, 'Sams', 62, '18:45', '18:05', 7798879185), (31, 'Costco', 63, '18:50', '19:15', 4995330373), (32, 'Costco', 64, '18:55', '19:20', 3389838241), (33, 'Costco', 65, '19:15', '19:35', 3426825578), (34, 'Trader Joes', 66, '20:00', '20:05', 7266703506), (35, 'Trader Joes ', 67, '20:35', '20:40', 2578136712);
UNLOCK TABLES;





--
-- Table structure for table `Payments`
--
CREATE TABLE Payments (
    username             VARCHAR(64)        NOT NULL,
    payment_name            VARCHAR(16)        NOT NULL,
    account_number        INT(16)        NOT NULL,
    routing_number            INT(16)        NOT NULL,
    PRIMARY KEY (username, payment_name),
CONSTRAINT us3 FOREIGN KEY(username) REFERENCES Userr (username) ON DELETE CASCADE  ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `Payments`
--

LOCK TABLES `Payments` WRITE; 
INSERT INTO `Payments` VALUES ('adepttimberry', 'Debt', 224136735, 985947465), ('adepttimberry', 'Check', 229335769, 393586216), ('adepttimberry', 'Visa', 453433338, 475782796), ('admirableneville', 'Check', 859232841, 547162669), ('admirableneville', 'American Express', 548461883, 936566668), ('admirableneville', 'Debt', 443396684, 118153385), ('admirableneville', 'Visa', 938225167, 937188583), ('bossywilfer', 'American Express', 178845786, 969972661), ('bossywilfer', 'Check', 752845415, 255275576), ('bossywilfer', 'Debt', 727423569, 816895789), ('bowedhannibal', 'Debt', 275233278, 828241964), ('bowedhannibal', 'Visa', 711934578, 654199468), ('bowedhannibal', 'Check', 268541329, 459319425), ('bowedhannibal', 'American Express', 391757451, 262514815), ('breakabletim', 'Visa', 479843748, 768442374), ('coldsnewkes', 'Visa', 419453712, 436877981), ('coldsnewkes', 'Debt', 978726843, 293343249), ('coldsnewkes', 'American Express', 276637386, 645336717), ('corruptbayton', 'Debt', 254367721, 433241274), ('corruptbayton', 'Check', 329113184, 561251217), ('corruptbayton', 'Visa', 393799114, 738933914), ('corruptbayton', 'American Express', 447648956, 369827941), ('dazzlingjohnny', 'Check', 434983631, 996114538), ('dazzlingjohnny', 'Debt', 453677155, 151621565), ('dazzlingjohnny', 'Visa', 244557625, 475358558), ('dazzlingjohnny', 'American Express', 868614372, 586699572), ('decimalherbert', 'Visa', 134237263, 412831959), ('decimalherbert', 'Check', 674693568, 497618842), ('decimalherbert', 'American Express', 738496917, 989719129), ('disfiguredalderman', 'Check', 939936896, 548117728), ('disfiguredalderman', 'Visa', 185826867, 365341381), ('disfiguredalderman', 'American Express', 374186112, 274366889), ('fainthannah', 'Check', 569493633, 725291753), ('fainthannah', 'American Express', 623393852, 582918438), ('firmdedlock', 'American Express', 877635171, 713989575), ('firmdedlock', 'Debt', 935488427, 147862112), ('freshpeltirogus', 'American Express', 265211653, 728361669), ('freshpeltirogus', 'Check', 288665872, 313144366), ('freshpeltirogus', 'Debt', 857537257, 283269352), ('frightenedsmallweed', 'American Express', 676595568, 614746883), ('frightenedsmallweed', 'Check', 592111452, 482788459), ('frightenedsmallweed', 'Debt', 968138394, 827692322), ('frightenedsmallweed', 'Visa', 274898237, 495524479), ('hurriedplornish', 'Debt', 636222285, 626825869), ('hurriedplornish', 'Visa', 559157981, 465223522), ('hurriedplornish', 'Check', 392235583, 954825597), ('hurriedplornish', 'American Express', 339197231, 348799723), ('inactivejane', 'Debt', 952371439, 138921459), ('inactivejane', 'Visa', 552386235, 989976499), ('inactivejane', 'American Express', 162265883, 271417791), ('inactivejane', 'Check', 521585611, 899182865), ('maddeningfladdock', 'American Express', 892855416, 915375484), ('maddeningfladdock', 'Check', 422985657, 245546988), ('maddeningfladdock', 'Visa', 382514276, 667231128), ('marvelousjinkins', 'American Express', 141432932, 995816235), ('marvelousjinkins', 'Debt', 214289528, 792556368), ('marvelousjinkins', 'Visa', 861589815, 843923475), ('marvelousjinkins', 'Check', 559373265, 617477844), ('melodicsparkler', 'Visa', 613512645, 653913937), ('melodicsparkler', 'American Express', 458648683, 261822483), ('melodicsparkler', 'Check', 631399139, 516682724), ('noxiousmould', 'Check', 534451118, 756313563), ('noxiousmould', 'American Express', 478788349, 562413535), ('noxiousmould', 'Visa', 139619193, 547863657), ('putridsnagsby', 'Visa', 255816926, 145641359), ('putridsnagsby', 'Check', 216352256, 878542628), ('putridsnagsby', 'American Express', 714574527, 372879695), ('putridsnagsby', 'Debt', 986516321, 897499545), ('rowdysteerforth', 'Visa', 888732334, 397579182), ('sablemagnus', 'Visa', 784736441, 776622738), ('sablemagnus', 'American Express', 152577638, 136557188), ('sablemagnus', 'Check', 336333515, 611199514), ('severelucy', 'Visa', 744548525, 656379928), ('severelucy', 'American Express', 162488547, 359184544), ('snobbymorleena', 'Visa', 183397537, 886223992), ('snobbymorleena', 'Check', 939523859, 488463677), ('snobbymorleena', 'American Express', 817749893, 815527188), ('tastyadams', 'Visa', 844181254, 295127233), ('tastyadams', 'American Express', 612115324, 582579615), ('tastyadams', 'Debt', 289127723, 217655562), ('tastyadams', 'Check', 196122283, 919732316), ('torpidkenge', 'Debt', 431996582, 541642496), ('torpidkenge', 'Visa', 936913267, 972877989), ('torpidkenge', 'American Express', 559873792, 229153196), ('torpidkenge', 'Check', 287271886, 427673487), ('unwrittensloppy', 'Debt', 933685543, 421876248), ('unwrittensloppy', 'Visa', 378863772, 781731763), ('unwrittensloppy', 'American Express', 557898165, 128163653), ('unwrittensloppy', 'Check', 964244214, 751917793), ('vitalbetty', 'Visa', 956166741, 125682616), ('welcomeleicester', 'American Express', 693824943, 258692133), ('wellmadeconkey', 'American Express', 585893344, 938262118), ('woozyprice', 'Debt', 654574336, 647211239), ('woozyprice', 'Check', 439687975, 816246288);
UNLOCK TABLES;





--
-- Table structure for table `Buyer`
--
CREATE TABLE Buyer (
    username            VARCHAR(64)        NOT NULL,
phone                CHAR(16)        NOT NULL,
address_id            INT(2)            NOT NULL,
default_payment        VARCHAR(16)        NOT NULL,
default_store_id      INT(16)             NOT NULL,
    PRIMARY KEY(username),
CONSTRAINT us FOREIGN KEY(username) REFERENCES Userr(username) ON DELETE CASCADE ON UPDATE CASCADE,
CONSTRAINT ad1 FOREIGN KEY(address_id) REFERENCES Address(id) ON DELETE CASCADE ON UPDATE CASCADE,
CONSTRAINT dsid FOREIGN KEY(default_store_id) REFERENCES GroceryStore(store_id) ON DELETE CASCADE ON UPDATE CASCADE
 ) ENGINE=InnoDB DEFAULT CHARSET=latin1;
 
--
-- Dumping data for table `Buyer`
--

LOCK TABLES `Buyer` WRITE; 
INSERT INTO `Buyer` VALUES ('coldsnewkes', 404466738, 1, 'Visa', 6), ('severelucy', 404737581, 2, 'Debt', 22), ('vitalbetty', 404834647, 3, 'Check', 29), ('welcomeleicester', 404376223, 4, 'American Express', 30), ('frightenedsmallweed', 404229474, 5, 'Debt', 14), ('corruptbayton', 404527538, 7, 'American Express', 7), ('unwrittensloppy', 404931962, 8, 'Visa', 22), ('dazzlingjohnny', 404941865, 9, 'Check', 8), ('wellmadeconkey', 404873273, 10, 'American Express', 35), ('melodicsparkler', 404848816, 11, 'American Express', 9), ('firmdedlock', 404948828, 12, 'Check', 10), ('torpidkenge', 404884464, 13, 'Visa', 2), ('maddeningfladdock', 404181323, 14, 'Debt', 17), ('noxiousmould', 404794841, 15, 'American Express', 9), ('admirableneville', 404888765, 16, 'Check', 2), ('hurriedplornish', 404625333, 17, 'American Express', 8), ('putridsnagsby', 404445867, 18, 'Visa', 9), ('marvelousjinkins', 404488296, 19, 'Debt', 9), ('decimalherbert', 404227614, 20, 'Check', 9), ('inactivejane', 404689185, 21, 'American Express', 16), ('bossywilfer', 404914121, 22, 'American Express', 3), ('freshpeltirogus', 404544358, 23, 'American Express', 13), ('snobbymorleena', 404241411, 24, 'Visa', 2), ('tastyadams', 404735117, 25, 'Check', 22), ('sablemagnus', 404931126, 26, 'Visa', 23), ('breakabletim', 404215927, 27, 'American Express', 5), ('rowdysteerforth', 404457524, 28, 'Check', 22), ('disfiguredalderman', 404919615, 29, 'Visa', 10), ('fainthannah', 404249388, 30, 'Check', 10), ('bowedhannibal', 404654644, 31, 'Debt', 4), ('adepttimberry', 404887516, 32, 'Debt', 1);
UNLOCK TABLES;

 



--
-- Table structure for table `manages`
--
CREATE TABLE manages (
    username            VARCHAR(64)        NOT NULL,
    store_address        INT(2)            NOT NULL,
    PRIMARY KEY(username, store_address),
CONSTRAINT us1 FOREIGN KEY(username) REFERENCES Userr (username) ON DELETE CASCADE ON UPDATE CASCADE,
CONSTRAINT ad0 FOREIGN KEY(store_address) REFERENCES Address (id) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `manages`
--

LOCK TABLES `manages` WRITE; 
INSERT INTO `manages` VALUES ('colorlessabbey', 33), ('optimalpluck', 34), ('quickestmortimer', 35), ('smoothbetsy', 36), ('pepsisilicon', 37), ('facebookoxygen', 38), ('hyundaimeitnerium', 39), ('colgatesulfur', 40), ('mcdonaldssodium', 41), ('amazonzirconium', 42), ('nescafeselenium', 43), ('chaneliridium', 44), ('heinzrutherfordium', 45), ('visahafnium', 46), ('chevroletberyllium', 47), ('guccinickel', 48), ('exxonindium', 49), ('pradaphosphorus', 50), ('ciscocobalt', 51), ('lancomegermanium', 52), ('foxbarium', 53), ('starbucksrhenium', 54), ('adidaslawrencium', 55), ('heinekenplatinum', 56), ('rolexfluorine', 57), ('toyotacarbon', 58), ('gillettetellurium', 59), ('lexuslanthanum', 60), ('boeingaluminum', 61), ('fordlead', 62), ('canonxenon', 63), ('burberrycopper', 64), ('malboroneodymium', 65), ('legothorium', 66), ('batmanisbetterthanmoonknight', 67);
UNLOCK TABLES;





--
-- Table structure for table `Orderr`
-- order_id, delivery_instructions, delivery_time, order_placed_date, order_placed_time
--
CREATE TABLE Orderr (
    order_id            INT(8)            NOT NULL,
    delivery_instructions        VARCHAR(256),
    delivery_time                VARCHAR(16)            NOT NULL,
    order_placed_date                VARCHAR(16)            NOT NULL,
    order_placed_time                VARCHAR(16)            NOT NULL,
    PRIMARY KEY (order_id)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `Orderr`
--

LOCK TABLES `Orderr` WRITE; 
INSERT INTO `Orderr` VALUES (13075, NULL, 'ASAP', '2019-07-10', '06:05'), (17466, NULL, '1', '2019-07-12', '15:35'), (20958, 'I have a party at 4 please hurry ', '2', '2019-07-06', '09:35'), (23231, 'avoid dog', '3', '2019-07-03', '05:50'), (24784, 'thank you!', '4', '2019-07-01', '07:25'), (31354, NULL, '5', '2019-07-06', '21:20'), (31541, NULL, '10', '2019-07-08', '17:15'), (32787, 'violent dog on property, leave in mailbox', '12', '2019-07-06', '06:25'), (33861, 'ring bell', '24', '2019-07-09', '05:35'), (34346, 'please bring me fruit', 'ASAP', '2019-07-07', '15:55'), (36188, NULL, '1', '2019-07-10', '06:35'), (40389, NULL, '2', '2019-07-12', '20:40'), (46403, NULL, '3', '2019-07-02', '09:40'), (47215, NULL, '4', '2019-07-07', '11:25'), (47361, 'sos', 'ASAP', '2019-07-04', '14:15'), (59856, NULL, '10', '2019-07-14', '08:30'), (62224, NULL, '12', '2019-07-10', '05:15'), (63145, "I haven't eaten in days", 'ASAP', '2019-07-01', '15:00'), (64677, 'leave at door', 'ASAP', '2019-07-14', '05:10'), (65334, 'Please keep meat separate from the rest.', 'ASAP', '2019-07-12', '10:15'), (67217, NULL, '2', '2019-07-04', '11:35'), (68211, 'no rush', 'ASAP', '2019-07-12', '11:40'), (68759, 'All the icecream in the same bag please.', '4', '2019-07-01', '07:05'), (71533, NULL, '5', '2019-07-05', '05:25'), (72039, NULL, 'ASAP', '2019-07-13', '10:40'), (78318, 'Thanks', 'ASAP', '2019-07-01', '21:25'), (80145, 'no rush', 'ASAP', '2019-07-13', '09:00'), (81845, NULL, 'ASAP', '2019-07-11', '14:55'), (87232, NULL, '1', '2019-07-01', '18:30'), (87897, "I won't be home, leave at front door please.", 'ASAP', '2019-07-08', '19:45'), (92049, NULL, '3', '2019-07-03', '09:20'), (94516, "if there's meat, don't let it get bad please. If you have a cooler, use it please.", '4', '2019-07-11', '16:50'), (96079, NULL, '5', '2019-07-03', '05:40'), (96350, NULL, '10', '2017-07-13', '16:45'), (99511, NULL, 'ASAP', '2017-07-01', '12:05');
UNLOCK TABLES;





--
-- Table structure for table `orderedBy`
--
CREATE TABLE orderedBy (
    order_id            INT(8)            NOT NULL,
    buyer_username        VARCHAR(64)        NOT NULL,
    PRIMARY KEY (order_id),
CONSTRAINT od1 FOREIGN KEY (order_id) REFERENCES Orderr (order_id) ON DELETE CASCADE ON UPDATE CASCADE,
CONSTRAINT bun FOREIGN KEY (buyer_username) REFERENCES Buyer (username) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=latin1;


--
-- Dumping data for table `orderedBy`
--


LOCK TABLES `orderedBy` WRITE; 
INSERT INTO `orderedBy` VALUES (64677, 'adepttimberry'), (62224, 'adepttimberry'), (71533, 'coldsnewkes'), (33861, 'corruptbayton'), (96079, 'corruptbayton'), (23231, 'dazzlingjohnny'), (13075, 'decimalherbert'), (32787, 'decimalherbert'), (36188, 'firmdedlock'), (68759, 'firmdedlock'), (24784, 'freshpeltirogus'), (59856, 'frightenedsmallweed'), (80145, 'hurriedplornish'), (92049, 'hurriedplornish'), (20958, 'hurriedplornish'), (46403, 'inactivejane'), (65334, 'maddeningfladdock'), (72039, 'maddeningfladdock'), (47215, 'melodicsparkler'), (67217, 'sablemagnus'), (68211, 'rowdysteerforth'), (99511, 'sablemagnus'), (47361, 'sablemagnus'), (81845, 'sablemagnus'), (63145, 'severelucy'), (17466, 'severelucy'), (34346, 'snobbymorleena'), (96350, 'snobbymorleena'), (94516, 'tastyadams'), (31541, 'tastyadams'), (87232, 'tastyadams'), (87897, 'torpidkenge'), (40389, 'torpidkenge'), (31354, 'torpidkenge'), (78318, 'unwrittensloppy');
UNLOCK TABLES;





--
-- Table structure for table `Item`
--
CREATE TABLE Item (
    item_id            INT(2)            NOT NULL,
    item_name        VARCHAR(64)        NOT NULL,
    food_group        VARCHAR(16)        NOT NULL,
    exp_date        VARCHAR(16)            NOT NULL,
    quantity        INT(8)            NOT NULL,
    listed_price        DECIMAL (8,2)    NOT NULL,    
    wholesale_price        DECIMAL (8,2)    NOT NULL,
    description        VARCHAR(256)    NOT NULL,
    PRIMARY KEY(item_id)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `Item`
--

LOCK TABLES `Item` WRITE; 
INSERT INTO `Item` VALUES (1, 'guavas', 'Produce', '2023-02-27', 3, 14.54, 6.19, '3 items of guava fruit'), (2, 'wild rice', 'Others', '2023-04-14', 1, 21.99, 22.78, '1 bag of wild rice'), (3, 'cilantro', 'Produce', '2024-06-12', 1, 23.26, 7.99, '1 bush of cilantro'), (4, 'Irish cream liqueur', 'Beverages', '2024-10-24', 7, 10.42, 11.28, '7 pack of irish creme liqueor'), (5, 'tomato sauce', 'Canned Goods', '2025-05-28', 7, 15.5, 22.9, '7 cans'), (6, 'flax seed', 'Others', '2025-10-20', 6, 16.41, 14.12, '6 pouches of flax seed'), (7, 'romaine lettuce', 'Produce', '2026-03-04', 1, 16.77, 7.29, '1 bunch of romaine lettuce'), (8, 'pomegranates', 'Produce', '2026-06-01', 1, 7.89, 5.32, '1 pomegranate'), (9, 'bok choy', 'Produce', '2027-02-02', 8, 17.62, 6.83, '8 bok choy'), (10, 'tarragon', 'Others', '2027-11-25', 10, 6.11, 11.85, '10 tarragon packets'), (11, 'mayonnaise', 'Dairy', '2028-02-03', 11, 18.57, 5.12, '11 mini mayonnaise packets'), (12, 'cloves', 'Others', '2028-10-26', 2, 7.77, 9.47, '2 cloves'), (13, 'allspice', 'Others', '2029-11-26', 10, 1.66, 6.91, '10 packets of allspice'), (14, 'cherries', 'Produce', '2030-07-31', 8, 17.96, 5.17, '8 cherries'), (15, 'tuna', 'Meat', '2030-12-23', 4, 12.91, 2.76, '4 fresh tuna steaks'), (16, 'ale', 'Beverages', '2032-01-07', 5, 2.06, 5.41, '5 bottles of ale'), (17, 'beets', 'Produce', '2032-01-09', 12, 5.37, 16.67, '12 beets'), (18, 'lemon juice', 'Beverages', '2033-08-16', 6, 21.79, 7.86, '6 bottles of lemon juice'), (19, 'cod', 'Meat', '2033-11-23', 5, 1.65, 19.76, '5 slabs of cod fish'), (20, 'bean sprouts', 'Produce', '2034-01-05', 12, 20.85, 22.8, '12 sprouts of bean'), (21, 'Worcestershire sauce', 'Beverages', '2035-03-21', 7, 4.73, 5.46, '7 bottles'), (22, 'date sugar', 'Baking Goods', '2035-06-27', 6, 9.34, 21.42, '6 packets of date sugar'), (23, 'sweet chili sauce', 'Beverages', '2035-11-30', 4, 1.74, 20.82, '4 bottles'), (24, 'sardines', 'Meat', '2036-10-16', 9, 6.82, 14.54, '9 fresh canned sardines'), (25, 'octopus', 'Meat', '2036-12-19', 6, 2.62, 24.87, '6 octopus legs'), (26, 'Canadian bacon', 'Meat', '2022-08-25', 11, 18.23, 2.29, '11 slices of bacon'), (27, 'mascarpone', 'Daiy', '2023-01-13', 7, 5.5, 9.19, '7 packets of mascarpone'), (28, 'pork', 'Meat', '2023-07-19', 9, 10.03, 11.17, '9 pieces of pork'), (29, 'sweet peppers', 'Produce', '2023-08-03', 3, 17.44, 19.38, '3 sweet pepers'), (30, 'pecans', 'Others', '2023-12-18', 2, 13.45, 6.74, '2 pecans'), (31, 'rosemary', 'Produce', '2024-10-25', 7, 8.71, 21.93, '7 branches of rosemary'), (32, 'beef', 'Meat', '2025-11-26', 7, 4.25, 9.62, '7 packets of ground beef'), (33, 'anchovies', 'Meat', '2026-10-15', 8, 17.96, 9.88, '8 anchovies in can'), (34, 'spaghetti squash', 'Produce', '2029-01-10', 7, 2.67, 12.55, '7 spaghetti squashes'), (35, 'cannellini beans', 'Canned Goods', '2029-02-28', 9, 7.16, 9.3, '9 cans of beans'), (36, 'Romano cheese', 'Dairy', '2029-04-20', 8, 16.75, 12.65, '8 oz of romano cheese'), (37, 'cooking wine', 'Beverages', '2029-12-06', 11, 14.93, 17.83, '11 mini bottles of white cooking wine'), (38, 'peanuts', 'Others', '2030-05-22', 1, 3.33, 6.53, '1 penut'), (39, 'crabs', 'Meat', '2030-12-20', 4, 17.33, 22.14, '4 live crabs '), (40, 'mozzarella', 'Dairy', '2032-01-30', 5, 2.98, 6.6, '5 mozzarella balls'), (41, 'vermouth', 'Beverages', '2032-08-13', 11, 2.04, 3.59, '11 mini bottles of vermouth'), (42, 'cranberries', 'Produce', '2032-10-01', 8, 13.45, 23.17, '8 cranberries'), (43, 'barley sugar', 'Baking Goods', '2032-11-04', 12, 10.88, 21.82, '12 bags of barley sugar'), (44, 'zest', 'Others', '2034-12-12', 8, 1.85, 12.49, '8 containers of lemon zest'), (45, 'baguette', 'Others', '2034-12-25', 10, 15.67, 16.36, '10 baguettes'), (46, 'sour cream', 'Dairy', '2035-01-10', 7, 24.21, 3.75, '7 containers of sour creme'), (47, 'prosciutto', 'Meat', '2035-05-18', 11, 8.17, 23.18, '11 slices of prosciutto'), (48, 'Kahlua', 'Beverages', '2035-07-18', 9, 6.99, 11.62, '9 mini bottles of Kahlua'), (49, 'squid', 'Meat', '2036-01-16', 11, 2.34, 5.74, '11 live baby squids'), (50, 'papayas', 'Produce', '2036-03-25', 8, 21.59, 18.33, '8 mini papayas');
UNLOCK TABLES;





--
-- Table structure for table `selectItem`
--
CREATE TABLE selectItem (
    item_id            INT(2)            NOT NULL,
    quantity            INT(8)            NOT NULL,
    order_id                INT(8)            NOT NULL,
    PRIMARY KEY (item_id, order_id),
CONSTRAINT od2 FOREIGN KEY (order_id) REFERENCES Orderr (order_id) ON DELETE CASCADE ON UPDATE CASCADE,
CONSTRAINT iid FOREIGN KEY (item_id) REFERENCES Item (item_id) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `selectItem`
--

LOCK TABLES `selectItem` WRITE; 
INSERT INTO `selectItem` VALUES (23, 8, 13075), (33, 3, 13075), (34, 1, 13075), (38, 2, 13075), (1, 14, 17466), (18, 6, 20958), (15, 4, 23231), (16, 1, 23231), (20, 1, 23231), (21, 5, 23231), (22, 13, 23231), (24, 9, 23231), (32, 2, 23231), (37, 5, 23231), (40, 15, 23231), (46, 5, 23231), (25, 5, 24784), (44, 4, 31354), (39, 1, 31541), (12, 1, 32787), (21, 2, 33861), (8, 1, 34346), (29, 8, 34346), (37, 5, 34346), (40, 7, 34346), (45, 12, 34346), (48, 7, 34346), (2, 13, 36188), (3, 3, 36188), (7, 14, 36188), (14, 9, 36188), (20, 11, 36188), (21, 13, 36188), (23, 8, 36188), (27, 7, 36188), (29, 4, 36188), (32, 3, 36188), (33, 4, 36188), (37, 10, 36188), (25, 4, 40389), (1, 8, 46403), (3, 3, 46403), (7, 3, 46403), (8, 4, 46403), (20, 7, 46403), (23, 5, 46403), (39, 9, 46403), (45, 15, 46403), (49, 9, 46403), (3, 15, 47215), (5, 1, 47215), (21, 10, 47215), (36, 5, 47215), (39, 13, 47215), (11, 6, 47361), (13, 3, 59856), (22, 5, 59856), (25, 8, 59856), (29, 8, 59856), (38, 12, 59856), (43, 12, 59856), (44, 15, 59856), (7, 15, 62224), (19, 6, 62224), (50, 13, 62224), (32, 13, 63145), (12, 6, 64677), (30, 6, 64677), (43, 3, 64677), (45, 3, 64677), (49, 9, 65334), (14, 4, 67217), (2, 1, 68211), (18, 8, 68759), (1, 14, 71533), (5, 12, 71533), (19, 12, 71533), (22, 2, 71533), (24, 13, 71533), (25, 11, 71533), (39, 11, 71533), (42, 11, 71533), (2, 15, 72039), (14, 5, 78318), (13, 9, 80145), (6, 9, 81845), (15, 1, 81845), (20, 6, 81845), (26, 12, 81845), (27, 3, 81845), (29, 3, 81845), (36, 12, 81845), (18, 2, 87232), (16, 4, 87897), (28, 13, 87897), (36, 13, 87897), (41, 5, 87897), (46, 11, 87897), (22, 13, 92049), (1, 13, 94516), (5, 10, 96079), (23, 10, 96079), (38, 13, 96079), (49, 15, 96079), (50, 4, 96079), (15, 13, 96350), (41, 10, 99511);
UNLOCK TABLES;





--
-- Table structure for table `orderFrom`
--
CREATE TABLE orderFrom (
    store_address_id        INT(2)            NOT NULL,
    order_id            INT(8)            NOT NULL,
    PRIMARY KEY (order_id),
CONSTRAINT ad2 FOREIGN KEY (store_address_id) REFERENCES GroceryStore (store_id) ON DELETE CASCADE ON UPDATE CASCADE,
CONSTRAINT od3 FOREIGN KEY (order_id) REFERENCES Orderr (order_id) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `orderFrom`
--

LOCK TABLES `orderFrom` WRITE; 
INSERT INTO `orderFrom` VALUES (15, 13075), (31, 17466), (17, 20958), (2, 23231), (19, 24784), (16, 31354), (2, 31541), (20, 32787), (6, 33861), (26, 34346), (31, 36188), (1, 40389), (1, 46403), (16, 47215), (2, 47361), (24, 59856), (16, 62224), (20, 63145), (13, 64677), (16, 65334), (29, 67217), (6, 68211), (26, 68759), (29, 71533), (13, 72039), (24, 78318), (2, 80145), (15, 81845), (20, 87232), (17, 87897), (20, 92049), (24, 94516), (2, 96079), (19, 96350), (2, 99511);
UNLOCK TABLES;





--
-- Table structure for table `soldAt`
--
CREATE TABLE soldAt (
    item_id                INT(2)            NOT NULL,
    store_id        INT(2)            NOT NULL,
PRIMARY KEY (item_id, store_id),
CONSTRAINT it FOREIGN KEY (item_id) REFERENCES Item (item_id) ON DELETE CASCADE ON UPDATE CASCADE,
CONSTRAINT ad3 FOREIGN KEY (store_id) REFERENCES GroceryStore (store_id) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=latin1;


--
-- Dumping data for table `soldAt`
--

LOCK TABLES `soldAt` WRITE; 
INSERT INTO `soldAt` VALUES (1, 13), (2, 16), (3, 13), (4, 16), (5, 29), (6, 6), (7, 2), (8, 2), (9, 15), (10, 20), (11, 31), (12, 26), (13, 19), (14, 24), (15, 2), (16, 20), (17, 17), (18, 1), (19, 16), (20, 24), (21, 13), (22, 24), (23, 8), (24, 17), (25, 27), (26, 10), (27, 20), (28, 22), (29, 30), (30, 26), (31, 14), (33, 17), (33, 4), (33, 7), (33, 18), (33, 9), (34, 4), (35, 24), (36, 8), (37, 17), (38, 27), (38, 10), (39, 20), (39, 22), (39, 30), (39, 26), (40, 14), (41, 17), (42, 4), (43, 13), (44, 16), (45, 29), (46, 6), (47, 2), (48, 2), (49, 15), (50, 20);
UNLOCK TABLES;





--
-- Table structure for table `deliveredBy`
--
CREATE TABLE deliveredBy (
    order_id            INT(8)            NOT NULL,
    deliverer_username        VARCHAR(64)        NOT NULL,
    is_delivered            BOOLEAN        NOT NULL,
    delivery_time                VARCHAR(16),
    delivery_date                VARCHAR(16),
    PRIMARY KEY(order_id),
CONSTRAINT od4 FOREIGN KEY (order_id) REFERENCES Orderr (order_id) ON DELETE CASCADE ON UPDATE CASCADE,
CONSTRAINT dun1 FOREIGN KEY (deliverer_username) REFERENCES Userr (username) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `deliveredBy`
--

LOCK TABLES `deliveredBy` WRITE; 
INSERT INTO `deliveredBy` VALUES (17466, 'spiffyjudith', 0, NULL, NULL), (31354, 'twinchicken', 0, NULL, NULL), (31541, 'teenyroads', 0, NULL, NULL), (34346, 'stylishtowlinson', 0, NULL, NULL), (40389, 'twinchicken', 0, NULL, NULL), (63145, 'shadowywestlock', 0, NULL, NULL), (78318, 'unknownswidger', 0, NULL, NULL), (81845, 'reasonablewrayburn', 0, NULL, NULL), (87232, 'teenyroads', 0, NULL, NULL), (87897, 'teenyroads', 0, NULL, NULL), (94516, 'stylishtowlinson', 0, NULL, NULL), (96350, 'stylishtowlinson', 0, NULL, NULL), (13075, 'chivalrouspotatoes', 1, '12:05', '2019-07-02'), (20958, 'chivalrouspotatoes', 1, '15:35', '2019-07-07'), (23231, 'chivalrouspotatoes', 1, '14:50', '2019-07-04'), (24784, 'chivalrouspotatoes', 1, '18:25', '2019-07-14'), (32787, 'chivalrouspotatoes', 1, '17:25', '2019-07-10'), (33861, 'chivalrouspotatoes', 1, '15:35', '2019-07-01'), (36188, 'chivalrouspotatoes', 1, '05:35', '2019-07-14'), (46403, 'chivalrouspotatoes', 1, '10:40', '2019-07-12'), (47215, 'inventivenickleby', 1, '13:25', '2019-07-04'), (47361, 'reasonablewrayburn', 1, '12:15', '2019-07-12'), (59856, 'chivalrouspotatoes', 1, '11:30', '2019-07-01'), (62224, 'chivalrouspotatoes', 1, '10:15', '2019-07-05'), (64677, 'chivalrouspotatoes', 1, '10:57', '2019-07-13'), (65334, 'downrightcorney', 1, '22:15', '2019-07-01'), (67217, 'languidtopsawyer', 1, '09:35', '2019-07-13'), (68211, 'methodicalcharity', 1, '15:40', '2019-07-11'), (68759, 'chivalrouspotatoes', 1, '19:05', '2019-07-01'), (71533, 'chivalrouspotatoes', 1, '20:25', '2019-07-08'), (72039, 'glumsmike', 1, '12:40', '2019-07-03'), (80145, 'chivalrouspotatoes', 1, '20:00', '2019-07-11'), (92049, 'chivalrouspotatoes', 1, '10:20', '2019-07-03'), (96079, 'chivalrouspotatoes', 1, '02:40', '2017-07-14'), (99511, 'reasonablewrayburn', 1, '12:35', '2017-07-01');
UNLOCK TABLES;

-- EOF