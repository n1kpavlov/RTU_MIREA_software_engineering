import java.util.List;

public interface FileComponent {
    void add(FileComponent fileComponent);
    void remove(FileComponent fileComponent);
    List<FileComponent> getChilds();
    String getName();
    void display(int depth);
}
