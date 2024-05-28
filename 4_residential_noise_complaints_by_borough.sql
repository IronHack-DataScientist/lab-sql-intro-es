SELECT borough, COUNT(*) AS num_residential_noise_complaints
FROM nyc_311_service_requests
WHERE complaint_type = 'Noise - Residential'
GROUP BY borough;
