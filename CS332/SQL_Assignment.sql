SELECT FName, LName, SSN FROM `employee` WHERE Salary=(SELECT MIN(Salary) FROM `employee`);

SELECT e.FName, e.LName FROM employee e, dependent d WHERE e.SSN=d.ESSN AND d.Relationship="Spouse" AND e.FName IN (SELECT e.FName FROM employee e, dependent d WHERE e.SSN=d.ESSN AND d.Relationship="Daughter") AND e.LName IN (SELECT e.LName FROM employee e, dependent d WHERE e.SSN=d.ESSN AND d.Relationship="Daughter");

SELECT e.FName, e.LName, p.PNo FROM employee e, works_on p WHERE e.SSN=p.ESSN AND e.LName IN ("Wong", "Borg", "English");

SELECT e.FName, e.LName, e.SSN, e.Salary FROM employee e, department d WHERE d.MGRSSN=e.SSN AND e.Salary>30000 AND e.Sex="M";

SELECT w.PNo, p.PName FROM employee e, works_on w, project p WHERE w.ESSN=e.SSN AND w.PNo=p.PNumber AND e.LName="Jabbar" AND w.PNo in (SELECT w.PNo FROM employee e, works_on w, project p WHERE w.ESSN=e.SSN AND w.PNo=p.PNumber AND e.LName="Narayan");

SELECT e.FName, e.LName, YEAR(CURRENT_DATE)-YEAR(d.Bdate) AS Age FROM employee e, dependent d WHERE e.SSN=d.ESSN AND YEAR(d.Bdate)>1970;

SELECT e.FName, e.LName, p.PName, w.Hours FROM employee e, project p, works_on w WHERE p.PLocation="Houston" AND p.PNumber=w.PNo AND w.ESSN=e.SSN;

SELECT e.FName, e.LName, (SELECT FName FROM employee WHERE SSN=e.SuperSSN) AS SupervisorFName,(SELECT LName FROM employee WHERE SSN=e.SuperSSN) AS SupervisorLName FROM employee e;

SELECT p.PName, e.FName, e.LName, p.PLocation FROM employee e, department d, project p WHERE p.DNum=d.DNumber AND d.MGRSSN=e.SSN;

SELECT e.FName, e.LName, e.Salary FROM employee e, department d WHERE d.MGRSSN=e.SSN AND e.Salary IN (SELECT MAX(e.Salary) FROM employee e, department d WHERE e.SSN=d.MGRSSN);