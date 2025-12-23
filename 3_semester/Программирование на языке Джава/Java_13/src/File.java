import java.util.List;

public class File implements FileComponent{
    private String name;

    public File(String name) {
        this.name = name;
    }

    @Override
    public void add(FileComponent fileComponent) {
        throw new UnsupportedOperationException();
    }

    @Override
    public void remove(FileComponent fileComponent) {
        throw new UnsupportedOperationException();
    }

    @Override
    public List<FileComponent> getChilds() {
        throw new UnsupportedOperationException();
    }

    @Override
    public String getName() {
        return name;
    }

    @Override
    public void display(int depth) {
        String indent = " ".repeat(depth * 4);
        System.out.println(indent + "- " + name + " (File)");
    }
}
