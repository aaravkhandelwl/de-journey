CREATE TABLE f1_results (
  driver VARCHAR(50),
  race VARCHAR(50),
  position INT,
  points INT
);
INSERT INTO f1_results VALUES
('Verstappen', 'Bahrain', 1, 25),
('Hamilton', 'Bahrain', 2, 18),
('Leclerc', 'Bahrain', 3, 15),
('Verstappen', 'Monaco', 2, 18),
('Hamilton', 'Monaco', 1, 25),
('Leclerc', 'Monaco', 4, 12);
-- Query 1: Rank drivers by total points
SELECT driver,
       SUM(points) as total_points,
       RANK() OVER (ORDER BY SUM(points) DESC) as ranking
FROM f1_results
GROUP BY driver;
-- Query 2: Best position per driver
SELECT driver,
       MIN(position) as best_finish,
       AVG(position) as avg_finish
FROM f1_results
GROUP BY driver;
-- Query 3: Points per race with running total
SELECT driver, race, points,
       SUM(points) OVER (PARTITION BY driver ORDER BY race) as running_total
FROM f1_results;