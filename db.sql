CREATE TABLE nodes (
id int auto_increment not null primary key,
active boolean not null default 1,
addtime TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
nuid varchar(200) not null,
ip varchar(129) not null, # imamo i ipv6, videti posle
cpu varchar(255) not null,
cpucores tinyint(10) not null,
arch varchar(7) not null,
kernel varchar(255) not null,
hostname varchar(255) not null,
ramtotal int not null,
disktotal int not null,
user varchar(64) not null,
subuser varchar(64) null,
reportlvl tinyint(3) not null default 1,
warnlvl tinyint(3) not null default 1
);

#INSERT INTO nodes (nuid, ip, cpu, cpucores, arch, kernel, hostname, ramtotal, disktotal, user) VALUES ("nekinuid2", "182.22.22.5", "AMD FX", 4, "i486", "4.2", "server1", "16000", "120", "nelebadnjak");


CREATE TABLE logs (
id int auto_increment not null primary key,
nuid varchar(64) not null,
lastactive timestamp not null,
ramfree int not null,
load int not null,
cputil tinyint(3) not null,
hdd int not null,
bandup int not null,
banddown int not null,
process int not null
);

CREATE TABLE users (
id int auto_increment not null primary key,
user varchar(64) not null,
password varchar(64) not null,
nodelimit int not null,
name varchar(64) not null,
surname varchar(64) not null,
email varchar(64) not null,
phone varchar(32) null,
company varchar(64) null,
authkey varchar(128) not null,
);

CREATE TABLE subusers (
id int auto_increment not null primary key,
adminuser varchar(64) not null,
user varchar(64) not null,
password varchar(128) not null,
authkey varchar(128) null
);

