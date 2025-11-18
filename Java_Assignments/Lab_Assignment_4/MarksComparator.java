import java.util.Comparator;

public class MarksComparator implements Comparator<Student> {
    @Override
    public int compare(Student s1, Student s2) {
        // Sort in Descending order (Highest marks first)
        if (s1.getMarks() < s2.getMarks()) return 1;
        if (s1.getMarks() > s2.getMarks()) return -1;
        return 0;
    }
}