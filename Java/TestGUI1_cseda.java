import javax.swing.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.io.IOException;
import java.lang.Process;

public class TestGUI1_cseda {

        public static void main( String[] args) throws IOException {
            ProcessBuilder pBuilder = new ProcessBuilder("python","C:\\Users\\super\\ForFunsies\\CSC380_Inficon_Supplier_Processing\\Python\\main.py","Vendor-Form.pdf");
            pBuilder.redirectErrorStream(true);

            JFrame frame = new JFrame("Test");
            JButton uploadButton = new JButton("Upload");

            Icon icon = new ImageIcon("C:\\Users\\super\\Downloads\\gifs&memes\\skeleton-dance.gif\"");

            uploadButton.setIcon(icon);

            uploadButton.setBounds(30,30,80,30);

            uploadButton.addActionListener(new ActionListener() {
                @Override
                public void actionPerformed(ActionEvent e) {
                    //System.exit(0);
                    try {
                        pBuilder.command();
                        Process fill = pBuilder.start();

                    } catch (IOException ex) {
                        throw new RuntimeException(ex);
                    }

                }
            });

            frame.add(uploadButton);



            frame.setSize(1200,720);
            frame.setLayout(null);
            frame.setVisible(true);
        }
    }
