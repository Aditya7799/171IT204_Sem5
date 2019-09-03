SELECT Fname,Minit,Lname,Address FROM EMPLOYEE WHERE Dno = (SELECT Dnumber FROM DEPARTMENT WHERE Dname = 'Administration');

SELECT SUM(Salary),MAX(Salary),MIN(Salary),AVG(Salary) FROM EMPLOYEE WHERE Dno = (SELECT Dnumber FROM DEPARTMENT WHERE Dname = 'Research');

SELECT COUNT(*) FROM EMPLOYEE WHERE Dno = (SELECT Dnumber FROM DEPARTMENT WHERE Dname = 'Administration');

SELECT p.Pnumber,p.Pname,COUNT(*) as EMPLOYEEs FROM PROJECT p, EMPLOYEE e, WORKS_ON w WHERE e.Ssn = w.Essn AND p.Pnumber = w.Pno GROUP BY p.Pnumber;

SELECT p.Pnumber,p.Pname,COUNT(*) as EMPLOYEEs FROM PROJECT p, EMPLOYEE e, WORKS_ON w WHERE e.Ssn = w.Essn AND p.Pnumber = w.Pno and p.Dnum = 5 GROUP BY p.Pnumber;

SELECT p.Pnumber, p.Dnum, e.Lname, e.Address from PROJECT p, EMPLOYEE e WHERE e.Ssn = (SELECT Mgr_ssn FROM DEPARTMENT WHERE Dnumber = p.Dnum) AND p.Plocation = 'Houston';

SELECT e.Fname,e.Lname,p.Pname FROM PROJECT p, EMPLOYEE e, WORKS_ON w WHERE e.Ssn = w.Essn AND p.Pnumber = w.Pno ORDER BY p.Dnum, e.Fname ASC, e.Lname DESC;

SELECT Fname,Minit,Lname FROM EMPLOYEE WHERE Super_ssn IS NULL;

SELECT Fname,Minit,Lname FROM EMPLOYEE WHERE Super_ssn IN (SELECT Ssn FROM EMPLOYEE WHERE Super_ssn = 987654321);

SELECT d.Dname, e.Fname, e.Minit, e.Lname, e.Salary FROM DEPARTMENT d, EMPLOYEE e WHERE d.Mgr_ssn = e.Ssn;

SELECT e.Fname,e.Minit,e.Lname,e1.Fname,e1.Minit,e1.Lname,e.Salary FROM EMPLOYEE e, EMPLOYEE e1 WHERE e.Super_ssn = e1.Ssn AND e.Dno = (SELECT Dnumber FROM DEPARTMENT WHERE Dname = 'Research');

SELECT p.Pname, d.Dname, COUNT(*), sum(w.Hours) FROM PROJECT p, DEPARTMENT d, EMPLOYEE e, WORKS_ON w WHERE p.Dnum = d.Dnumber AND e.Ssn = w.Essn AND p.Pnumber = w.Pno AND p.Pnumber = w.Pno GROUP BY p.Pnumber;

SELECT p.Pname, d.Dname, COUNT(*), sum(w.Hours) FROM PROJECT p, DEPARTMENT d, EMPLOYEE e, WORKS_ON w WHERE p.Dnum = d.Dnumber AND e.Ssn = w.Essn AND p.Pnumber = w.Pno GROUP BY p.Pnumber HAVING Count(*)>1;

SELECT e.Fname,e.Minit,e.Lname FROM EMPLOYEE e, PROJECT p, WORKS_ON w WHERE e.Ssn = w.Essn AND w.Pno = p.Pnumber AND p.Dnum = 5;

SELECT e.Fname,e.Minit,e.Lname FROM EMPLOYEE e, PROJECT p, WORKS_ON w WHERE w.Essn = e.Ssn AND w.Pno = p.Pnumber and p.Pname = 'ProductX' AND w.Hours > 10;

SELECT e.Fname,e.Minit,e.Lname FROM EMPLOYEE e, DEPENDENT d WHERE e.Fname = d.DEPENDENT_name;

SELECT e.Fname,e.Minit,e.Lname FROM EMPLOYEE e, EMPLOYEE e1 WHERE e.Super_ssn = e1.Ssn and e1.Fname = 'Franklin' and e1.Lname = 'Wong';

SELECT p.Pname, SUM(w.Hours) FROM PROJECT p, WORKS_ON w WHERE w.Pno = p.Pnumber GROUP BY p.Pnumber;

SELECT AVG(Salary) FROM EMPLOYEE WHERE Sex = 'F';
