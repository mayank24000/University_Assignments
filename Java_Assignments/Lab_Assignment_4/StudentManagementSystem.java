    import java.util.Scanner;

    public class StudentManagementSystem {
        public static void main(String[] args) {
            StudentManager manager = new StudentManager();
            Scanner scanner = new Scanner(System.in);
            int choice;

            do {
                System.out.println("===== Capstone Student Menu =====");
                System.out.println("1. Add Student");
                System.out.println("2. View All Students");
                System.out.println("3. Search by Name");
                System.out.println("4. Delete by Name");
                System.out.println("5. Sort by Marks");
                System.out.println("6. File Utilities (Attributes/RandomAccess)");
                System.out.println("7. Save and Exit");
                System.out.print("Enter choice: ");
                
                try {
                    choice = Integer.parseInt(scanner.nextLine());
                } catch (NumberFormatException e) {
                    choice = 0;
                }

                switch (choice) {
                    case 1:
                        try {
                            System.out.print("Enter Roll No: ");
                            int roll = Integer.parseInt(scanner.nextLine());
                            System.out.print("Enter Name: ");
                            String name = scanner.nextLine();
                            System.out.print("Enter Email: ");
                            String email = scanner.nextLine();
                            System.out.print("Enter Course: ");
                            String course = scanner.nextLine();
                            System.out.print("Enter Marks: ");
                            double marks = Double.parseDouble(scanner.nextLine());

                            manager.addStudent(new Student(roll, name, email, course, marks));
                        } catch (Exception e) {
                            System.out.println("Invalid Input. Please try again.");
                        }
                        break;
                    case 2:
                        manager.viewAllStudents();
                        break;
                    case 3:
                        System.out.print("Enter Name to search: ");
                        String searchName = scanner.nextLine();
                        manager.searchByName(searchName);
                        break;
                    case 4:
                        System.out.print("Enter Name to delete: ");
                        String delName = scanner.nextLine();
                        manager.deleteByName(delName);
                        break;
                    case 5:
                        manager.sortByMarks();
                        break;
                    case 6:
                        manager.showTechDetails();
                        break;
                    case 7:
                        manager.saveAndExit();
                        System.out.println("Exiting system...");
                        break;
                    default:
                        System.out.println("Invalid choice!");
                }
            } while (choice != 7);

            scanner.close();
        }
    }