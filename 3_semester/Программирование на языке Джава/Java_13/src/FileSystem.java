public class FileSystem {
    public static void main(String[] args) {
        Directory root = new Directory("root");
        Directory usr = new Directory("usr");
        Directory local = new Directory("local");
        File file1 = new File("file1.txt");
        File file2 = new File("file2.jpg");
        Directory etc = new Directory("etc");
        File file3 = new File("config.ini");

        root.add(usr);
        root.add(local);
        usr.add(file1);
        usr.add(file2);
        local.add(etc);
        etc.add(file3);

        System.out.println("File System:");
        root.display(0);
    }
}