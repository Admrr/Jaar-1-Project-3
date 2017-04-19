CREATE TABLE metro (
wijk VARCHAR(255),
wijkoppervlakte_km2 FLOAT,
aantal_stations INT);

INSERT INTO metro (wijk, wijkoppervlakte_km2, aantal_stations)
VALUES ('Centrum', 4.81, 9),
('Delfshaven', 5.8, 5),
('Overschie', 15.80, NULL),
('Noord', 5.37, 1),
('Hillegersberg_Schiebroek', 13.26, 2),
('Kralingen_Crooswijk', 12.9, 3),
('Feijenoord', 6.44, 4),
('Ijsselmonde', 13.12, NULL),
('Prins_Alexander', 20.24, 10),
('Charlois', 10.0, 2);