-- 急诊滞留 >4h 实时监控
SELECT 
    p.pat_name,
    v.visit_no,
    v.triage_time,
    TIMESTAMPDIFF(MINUTE, v.triage_time, NOW()) / 60.0 AS los_hours,
    b.bed_code,
    v.current_status
FROM his_visit v
JOIN his_patient p ON v.pat_id = p.pat_id
LEFT JOIN his_bed_assign b ON v.visit_id = b.visit_id 
    AND b.is_current = 1
WHERE v.dept_code = 'ED'
  AND v.status IN ('TRIAGE', 'RESCUE', 'OBSERVATION')
  AND v.discharge_time IS NULL
  AND TIMESTAMPDIFF(MINUTE, v.triage_time, NOW()) > 240
ORDER BY los_hours DESC;
