use gamemanager;
select * from characters;
select * from Players
select * from item
drop table characters
drop table Players
CREATE TABLE Players (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL,
    passwords VARCHAR(255) NOT NULL,
    country ENUM('Korea', 'USA', 'Japan', 'India') NOT NULL
);


CREATE TABLE item (
    item_id INT PRIMARY KEY AUTO_INCREMENT,
    item_name VARCHAR(255) NOT NULL,
    item_type VARCHAR(255) NOT NULL,
    item_rarity VARCHAR(255) NOT NULL
);
CREATE TABLE Characters (
    id INT AUTO_INCREMENT PRIMARY KEY,
    player_email VARCHAR(255),
    character_name VARCHAR(255) NOT NULL,
    character_class VARCHAR(255) NOT NULL,
    character_gender VARCHAR(255) NOT NULL,
    FOREIGN KEY (player_email) REFERENCES Players(email)
);
ALTER TABLE Players
ADD INDEX idx_players_email (email);


CREATE INDEX idx_players_id ON Players (id);

select * from characters
select * from Players

CREATE TABLE skills (
    skill_id INT PRIMARY KEY AUTO_INCREMENT,
    skill_name VARCHAR(255) NOT NULL,
    skill_type VARCHAR(255) NOT NULL,
    skill_damage INT NOT NULL
);

INSERT INTO skills (skill_name, skill_type, skill_damage) VALUES
('Fireball', 'Fire', 80),
('Healing Touch', 'Healing', 0),
('Thunderstrike', 'Lightning', 120),
('Stealthy Strike', 'Stealth', 100),
('Ice Lance', 'Ice', 90),
('Earthquake', 'Earth', 150),
('Arcane Blast', 'Arcane', 110),
('Poison Dagger', 'Poison', 70),
('Holy Smite', 'Holy', 130),
('Shadow Bolt', 'Shadow', 95);


CREATE TABLE zones (
    zone_id INT PRIMARY KEY AUTO_INCREMENT,
    zone_name VARCHAR(255) NOT NULL,
    zone_level INT NOT NULL,
    zone_type VARCHAR(255) NOT NULL
);

INSERT INTO zones (zone_name, zone_level, zone_type) VALUES
('Emerald Valley', 1, 'Residential'),
('Skyline Plaza', 2, 'Commercial'),
('Ironworks District', 1, 'Industrial'),
('Sunset Heights', 3, 'Residential'),
('Harmony Square', 2, 'Commercial'),
('Innovation Park', 1, 'Industrial'),
('Tranquil Gardens', 2, 'Residential'),
('Oceanfront Promenade', 3, 'Commercial'),
('Luminary Heights', 1, 'Industrial'),
('Serenity Springs', 2, 'Residential');


CREATE TABLE quests (
    quest_id INT PRIMARY KEY AUTO_INCREMENT,
    quest_name VARCHAR(255) NOT NULL,
    quest_type VARCHAR(255) NOT NULL,
    quest_reward VARCHAR(255) NOT NULL
);

CREATE TABLE guild (
    guild_id INT PRIMARY KEY AUTO_INCREMENT,
    guild_name VARCHAR(255) NOT NULL,
    guild_level INT NOT NULL,
    guild_master VARCHAR(255) NOT NULL
);

INSERT INTO guild (guild_name, guild_level, guild_master) VALUES
('Warriors of Valor', 5, 'Aragorn'),
('Mystic Enclave', 3, 'Sorceress'),
('Shadow Assassins', 4, 'Nightblade'),
('Divine Sentinels', 6, 'Paladin'),
('Arcane Order', 2, 'Archmage'),
('Iron Legion', 4, 'Warlord'),
('Sapphire Sirens', 3, 'Siren Queen'),
('Order of the Phoenix', 5, 'Phoenix Knight'),
('Silent Shadows', 3, 'Shadowdancer'),
('Guardians of Gaia', 4, 'Druid');


CREATE TABLE server (
    server_id INT PRIMARY KEY AUTO_INCREMENT,
    server_name VARCHAR(255) NOT NULL,
    server_region VARCHAR(255) NOT NULL,
    server_capacity INT NOT NULL
);

INSERT INTO server (server_name, server_region, server_capacity) VALUES
('Alpha', 'North America', 100),
('Beta', 'Europe', 80),
('Gamma', 'Asia', 120),
('Delta', 'South America', 60),
('Epsilon', 'Australia', 40),
('Zeta', 'Africa', 50),
('Eta', 'North America', 90),
('Theta', 'Europe', 110),
('Iota', 'Asia', 70),
('Kappa', 'South America', 30);


CREATE TABLE transaction (
    transaction_id INT PRIMARY KEY AUTO_INCREMENT,
    item_id INT NOT NULL,
    player_email VARCHAR(255) NOT NULL,
    transaction_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    transaction_type VARCHAR(255) NOT NULL,
    FOREIGN KEY (item_id) REFERENCES item(item_id),
    FOREIGN KEY (player_email) REFERENCES Players(email)
);

CREATE TABLE log (
    log_id INT PRIMARY KEY AUTO_INCREMENT,
    log_message VARCHAR(255) NOT NULL,
    log_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

INSERT INTO log (log_message) VALUES
('Error: Database connection failed'),
('Warning: Insufficient disk space'),
('Information: User logged in'),
('Error: File not found'),
('Information: New user registered'),
('Warning: High CPU usage detected'),
('Information: Backup completed successfully'),
('Warning: Server response time is high'),
('Error: Invalid input detected'),
('Information: Application updated to version 2.0');

select * from log

select * from item

INSERT INTO quests (quest_name, quest_type, quest_reward) VALUES
    ('The Lost Relic', 'Exploration', 'Ancient Artifact'),
    ('A Knights Journey', 'Combat', 'Knight Armor'),
    ('The Enchanted Forest', 'Adventure', 'Magic Staff'),
    ('Mysteries of the Deep', 'Diving', 'Treasure Chest'),
    ('The Secret Recipe', 'Cooking', 'Master Chef Hat'),
    ('The Haunted Manor', 'Horror', 'Ghostly Pendant'),
    ('The Golden Key', 'Puzzle', 'Unlocking Ability'),
    ('The Dragons Lair', 'Boss Battle', 'Legendary Sword'),
    ('The Crystal Caves', 'Mining', 'Rare Gemstone'),
    ('The Time Traveler', 'Time Travel', 'Eternal Timepiece');
    
select * from quests
