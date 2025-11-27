import java.io.*;
import java.util.ArrayList;
import java.util.List;

public class FileUtil {
    private static final String FILE_NAME = "students.txt";
    public static List<Student> readStudentsFromFile() {
        List<Student> students = new ArrayList<>();
        File file = new File(FILE_NAME);

        if (!file.exists()) {
            System.out.println("File not found. A new one will be created upon save.");
            return students;
        }

        try (BufferedReader br = new BufferedReader(new FileReader(file))) {
            String line;
            System.out.println("Loaded students from file:");
            while ((line = br.readLine()) != null) {
                String[] data = line.split(",");
                if (data.length == 5) {
                    Student s = new Student(
                            Integer.parseInt(data[0]),
                            data[1],
                            data[2],
                            data[3],
                            Double.parseDouble(data[4])
                    );
                    students.add(s);
                    System.out.println(s);
                }
            }
        } catch (IOException e) {
            System.err.println("Error reading file: " + e.getMessage());
        }
        return students;
    }
    public static void writeStudentsToFile(List<Student> students) {
        try (BufferedWriter bw = new BufferedWriter(new FileWriter(FILE_NAME))) {
            for (Student s : students) {
                bw.write(s.toCSV());
                bw.newLine();
            }
            System.out.println("Records saved successfully.");
        } catch (IOException e) {
            System.err.println("Error writing to file: " + e.getMessage());
        }
    }

    public static void displayFileAttributes() {
        File file = new File(FILE_NAME);
        if (file.exists()) {
            System.out.println("\n--- File Attributes ---");
            System.out.println("File Name: " + file.getName());
            System.out.println("Absolute Path: " + file.getAbsolutePath());
            System.out.println("Writeable: " + file.canWrite());
            System.out.println("Readable: " + file.canRead());
            System.out.println("File Size: " + file.length() + " bytes");
            System.out.println("-----------------------");
        }
    }

    public static void demonstrateRandomAccess() {
        System.out.println("\n--- RandomAccessFile Demo ---");
        try (RandomAccessFile raf = new RandomAccessFile(FILE_NAME, "r")) {
            raf.seek(0)
            System.out.println("First line read via RandomAccessFile:");
            System.out.println(raf.readLine());
        } catch (FileNotFoundException e) {
            System.out.println("File not created yet.");
        } catch (IOException e) {
            System.err.println("Error in RandomAccessFile: " + e.getMessage());
        }
    }
}