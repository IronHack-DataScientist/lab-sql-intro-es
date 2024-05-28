SELECT complaint_type, COUNT(*) AS num_complaints
FROM nyc_311_service_requests
GROUP BY complaint_type
ORDER BY num_complaints DESC
LIMIT 5;
