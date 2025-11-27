import model.Student;
import service.StudentManager;
import util.StudentNotFoundException;

import java.util.Scanner;
public class Main {
    private static StudentManager studentManager;
    private static Scanner scanner;

    public static void main(String[] args) {
        studentManager = new StudentManager();
        scanner = new Scanner(System.in);

        try {
            studentManager.loadFromFile();
        } catch (Exception e) {
            System.err.println("⚠ Warning: " + e.getMessage());
        }

        boolean exit = false;

        System.out.println("╔════════════════════════════════════════════════╗");
        System.out.println("║   STUDENT RECORD MANAGEMENT SYSTEM             ║");
        System.out.println("║   Capstone Project                             ║");
        System.out.println("╚════════════════════════════════════════════════╝");

        while (!exit) {
            try {
                displayMenu();
                int choice = getChoice();

                switch (choice) {
                    case 1:
                        addStudent();
                        break;
                    case 2:
                        viewAllStudents();
                        break;
                    case 3:
                        searchByName();
                        break;
                    case 4:
                        deleteByName();
                        break;
                    case 5:
                        sortByMarks();
                        break;
                    case 6:
                        updateStudent();
                        break;
                    case 7:
                        saveAndExit();
                        exit = true;
                        break;
                    default:
                        System.out.println("\n⚠ Invalid choice! Please enter 1-7.");
                }
            } catch (Exception e) {
                System.err.println("\n✗ Error: " + e.getMessage());
                scanner.nextLine();
            }
        }

        scanner.close();
    }

    private static void displayMenu() {
        System.out.println("\n╔════════════════════════════════════════════════╗");
        System.out.println("║        CAPSTONE STUDENT MENU                   ║");
        System.out.println("╠════════════════════════════════════════════════╣");
        System.out.println("║  1. Add Student                                ║");
        System.out.println("║  2. View All Students                          ║");
        System.out.println("║  3. Search by Name                             ║");
        System.out.println("║  4. Delete by Name                             ║");
        System.out.println("║  5. Sort by Marks                              ║");
        System.out.println("║  6. Update Student                             ║");
        System.out.println("║  7. Save and Exit                              ║");
        System.out.println("╚════════════════════════════════════════════════╝");
        System.out.print("Enter choice: ");
    }

    private static int getChoice() {
        try {
            int choice = scanner.nextInt();
            scanner.nextLine();
            return choice;
        } catch (Exception e) {
            scanner.nextLine();
            return -1;
        }
    }

    private static void addStudent() {
        try {
            System.out.println("\n========== Add New Student ==========");
            Student student = new Student();
            student.inputDetails(scanner);
            studentManager.addStudent(student);
        } catch (Exception e) {
            System.err.println("\n✗ Failed to add student: " + e.getMessage());
        }
    }

    private static void viewAllStudents() {
        try {
            studentManager.viewAllStudents();
        } catch (Exception e) {
            System.err.println("\n✗ Error viewing students: " + e.getMessage());
        }
    }

    private static void searchByName() {
        try {
            System.out.println("\n========== Search Student ==========");
            System.out.print("Enter name to search: ");
            String name = scanner.nextLine().trim();

            if (name.isEmpty()) {
                System.out.println("\n⚠ Name cannot be empty!");
                return;
            }

            Student student = studentManager.searchStudent(name);
            System.out.println("\n✓ Student Found!");
            System.out.println("\n--- Student Information ---");
            student.displayDetails();
        } catch (StudentNotFoundException e) {
            System.err.println("\n✗ " + e.getMessage());
        } catch (Exception e) {
            System.err.println("\n✗ Error during search: " + e.getMessage());
        }
    }

    private static void deleteByName() {
        try {
            System.out.println("\n========== Delete Student ==========");
            System.out.print("Enter name to delete: ");
            String name = scanner.nextLine().trim();

            if (name.isEmpty()) {
                System.out.println("\n⚠ Name cannot be empty!");
                return;
            }

            System.out.print("Are you sure you want to delete this student? (yes/no): ");
            String confirm = scanner.nextLine().trim();

            if (confirm.equalsIgnoreCase("yes") || confirm.equalsIgnoreCase("y")) {
                studentManager.deleteStudent(name);
            } else {
                System.out.println("\n✗ Deletion cancelled.");
            }
        } catch (StudentNotFoundException e) {
            System.err.println("\n✗ " + e.getMessage());
        } catch (Exception e) {
            System.err.println("\n✗ Error during deletion: " + e.getMessage());
        }
    }

    private static void sortByMarks() {
        try {
            if (studentManager.getStudentCount() == 0) {
                System.out.println("\n⚠ No students to sort!");
                return;
            }
            studentManager.sortByMarks();
        } catch (Exception e) {
            System.err.println("\n✗ Error during sorting: " + e.getMessage());
        }
    }

    private static void updateStudent() {
        try {
            System.out.println("\n========== Update Student ==========");
            System.out.print("Enter Roll No of student to update: ");
            int rollNo = scanner.nextInt();
            scanner.nextLine();

            System.out.println("\nEnter new details:");
            Student updatedStudent = new Student();
            updatedStudent.inputDetails(scanner);
            updatedStudent.setRollNo(rollNo);

            studentManager.updateStudent(rollNo, updatedStudent);
        } catch (StudentNotFoundException e) {
            System.err.println("\n✗ " + e.getMessage());
        } catch (Exception e) {
            System.err.println("\n✗ Failed to update student: " + e.getMessage());
            scanner.nextLine();
        }
    }

    private static void saveAndExit() {
        try {
            studentManager.saveToFile();
            System.out.println("\n╔════════════════════════════════════════════════╗");
            System.out.println("║  Thank you for using the Student Management   ║");
            System.out.println("║  System. All records have been saved.          ║");
            System.out.println("║  Goodbye!                                      ║");
            System.out.println("╚════════════════════════════════════════════════╝");
        } catch (Exception e) {
            System.err.println("\n✗ Error saving data: " + e.getMessage());
            System.out.println("Exiting anyway...");
        }
    }
}