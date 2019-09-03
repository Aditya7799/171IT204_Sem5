SELECT Fname,Minit,Lname,Address FROM employee WHERE Dno = (SELECT Dnumber FROM department WHERE Dname = 'Administration');

SELECT SUM(Salary),MAX(Salary),MIN(Salary),AVG(Salary) FROM employee WHERE Dno = (SELECT Dnumber FROM department WHERE Dname = 'Research');

SELECT COUNT(*) FROM employee WHERE Dno = (SELECT Dnumber FROM department WHERE Dname = 'Administration');

SELECT p.Pno,p.Pname,COUNT(*) as employees FROM project p, employee e, works_on w WHERE e.Ssn = w.Essn AND p.Dnum = w.Pno GROUP BY p.Pno;

SELECT p.Pno,p.Pname,COUNT(*) as employees FROM project p, employee e, works_on w WHERE e.Ssn = w.Essn AND p.Dnum = w.Pno and p.Dnum = 5 GROUP BY p.Pno;

SELECT p.Pno, p.Dnum, e.Lname, e.Address from project p, employee e WHERE e.Ssn = (SELECT Mgr_ssr FROM department WHERE Dnumber = p.Dnum) AND p.Plocation = 'Houston';

SELECT * FROM project p, employee e, works_on w WHERE e.Ssn = w.Essn AND p.Dnum = w.Pno ORDER BY p.Dnum, e.Fname ASC, e.Lname DESC;

SELECT Fname,Minit,Lname FROM employee WHERE Super_ssn IS NULL;

SELECT Fname,Minit,Lname FROM employee WHERE Super_ssn IN (SELECT Ssn FROM employee WHERE Super_ssn = 987654321);

SELECT d.Dname, e.Fname, e.Minit, e.Lname, e.Salary FROM department d, employee e WHERE d.Mgr_ssr = e.Ssn;

SELECT e.Fname,e.Minit,e.Lname,e1.Fname,e1.Minit,e1.Lname,e.Salary FROM employee e, employee e1 WHERE e.Super_ssn = e1.Ssn AND e.Dno = (SELECT Dnumber FROM department WHERE Dname = 'Research');

SELECT p.Pname, d.Dname, COUNT(*), sum(w.Hours) FROM project p, department d, employee e, works_on w WHERE p.Dnum = d.Dnumber AND e.Ssn = w.Essn AND p.Pno = w.Pno AND p.Pno = w.Pno GROUP BY p.Pno;

SELECT p.Pname, d.Dname, COUNT(*), sum(w.Hours) FROM project p, department d, employee e, works_on w WHERE p.Dnum = d.Dnumber AND e.Ssn = w.Essn AND p.Pno = w.Pno AND (SELECT COUNT(*) FROM employee) > 1 GROUP BY p.Pno;

SELECT e.Fname,e.Minit,e.Lname FROM employee e, project p, works_on w WHERE e.Ssn = w.Essn AND w.Pno = p.Pno AND p.Dnum = 5;

SELECT e.Fname,e.Minit,e.Lname FROM employee e, project p, works_on w WHERE w.Essn = e.Ssn AND w.Pno = p.Pno and p.Pname = 'ProductX' AND w.Hours > 10;

SELECT e.Fname,e.Minit,e.Lname FROM employee e, dependent d WHERE e.Fname = d.Dependent_name;

SELECT e.Fname,e.Minit,e.Lname FROM employee e, employee e1 WHERE e.Super_ssn = e1.Ssn and e1.Fname = 'Franklin' and e1.Lname = 'Wong';

SELECT p.Pname, SUM(w.Hours) FROM project p, works_on w WHERE w.Pno = p.Pno GROUP BY p.Pno;

SELECT AVG(Salary) FROM employee WHERE Sex = 'F';
