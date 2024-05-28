SELECT borough, COUNT(*) AS num_complaints
FROM nyc_311_service_requests
GROUP BY borough;
