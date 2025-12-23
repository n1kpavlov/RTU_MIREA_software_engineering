import java.util.ArrayList;
import java.util.List;

public class Directory implements FileComponent{
    private String name;
    private List<FileComponent> components = new ArrayList<>();

    public Directory(String name) {
        this.name = name;
    }

    @Override
    public void add(FileComponent fileComponent) {
        components.add(fileComponent);
    }

    @Override
    public void remove(FileComponent fileComponent) {
        components.remove(fileComponent);
    }

    @Override
    public List<FileComponent> getChilds() {
        return components;
    }

    @Override
    public String getName() {
        return name;
    }

    @Override
    public void display(int depth) {
        String indent = " ".repeat(depth * 4);
        System.out.println(indent + "- " + name + " (Directory)");
        for (FileComponent component : components) {
            component.display(depth + 1);
        }
    }
}
