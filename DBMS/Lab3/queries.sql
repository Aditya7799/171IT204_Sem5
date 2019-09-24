SELECT pt.name AS "Patient",
       p.name AS "Primary care Physician"
FROM Patient pt
JOIN PhysicianE p ON pt.PCP=p.EmployeeID
WHERE pt.PCP NOT IN
    (SELECT Head
     FROM Department);



SELECT pt.name AS "Patient",
       p.name AS "Primary Physician",
       n.name AS "Nurse"
FROM Appointment a
JOIN Patient pt ON a.Patient=pt.SSN
JOIN Nurse n ON a.PrepNurse=n.EmployeeID
JOIN PhysicianE p ON pt.PCP=p.EmployeeID
WHERE a.Patient IN
    (SELECT Patient
     FROM Appointment a
     GROUP BY a.Patient
     HAVING count(*)>=2)
  AND n.Registered=1
ORDER BY pt.Name;


SELECT pt.name AS "Patient",
       p.name AS "Primary Physician",
       pd.cost AS "Procedure Cost"
FROM Patient pt
JOIN Undergoes u ON u.Patient=pt.SSN
JOIN PhysicianE p ON pt.PCP=p.EmployeeID
JOIN Procedures pd ON u.Procedures=pd.Code
WHERE pd.cost>5000;


SELECT p.name AS "Physician",
       p.position AS "Position",
       pr.name AS "Procedure",
       u.DateUndergoes AS "Date of Procedure",
       pt.name AS "Patient",
       t.CertificationExpires AS "Expiry Date of Certificate"
FROM PhysicianE p,
     Undergoes u,
     Patient pt,
     Procedures pr,
     Trained_In t
WHERE u.Patient = pt.SSN
  AND u.Procedures = pr.Code
  AND u.Physician = p.EmployeeID
  AND pr.Code = t.Treatment
  AND p.employeeid = t.Physician
  AND u.DateUndergoes > t.CertificationExpires;




SELECT p.name AS "Physician",
       pr.name AS "Procedure",
       u.DateUndergoes,
       pt.Name AS "Patient"
FROM PhysicianE p,
     Undergoes u,
     Patient pt,
     Procedures pr
WHERE u.Patient = pt.SSN
AND u.Procedures = pr.Code
AND u.Physician = p.EmployeeID
AND NOT EXISTS
(SELECT *
    FROM Trained_In t
    WHERE t.Treatment = u.Procedures
    AND t.Physician = u.Physician );