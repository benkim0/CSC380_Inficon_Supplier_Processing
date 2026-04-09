import javax.swing.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.io.IOException;
import java.lang.Process;

public class TestGUI1_cseda {

        public static void main( String[] args) throws IOException {
            ProcessBuilder pBuilder = new ProcessBuilder("\"C:\\Users\\super\\AppData\\Local\\Programs\\Python\\Python314\\python.exe\"","C:\\Users\\super\\ForFunsies\\CSC380_Inficon_Supplier_Processing\\Python\\main.py","C:\\Users\\super\\ForFunsies\\CSC380_Inficon_Supplier_Processing\\Python\\Vendor-Form.pdf");
            pBuilder.redirectErrorStream(true);
            pBuilder.redirectOutput(ProcessBuilder.Redirect.INHERIT);

            JFrame frame = new JFrame("Test");
            JButton uploadButton = new JButton("Execute");


            uploadButton.setBounds(30,30,200,30);

            uploadButton.addActionListener(new ActionListener() {
                @Override
                public void actionPerformed(ActionEvent e) {
                    try {

                        Process fill = pBuilder.start();

                    } catch (IOException ex) {
                        throw new RuntimeException(ex);
                    }

                }
            });

            frame.add(uploadButton);

            frame.setSize(300,200);
            frame.setLayout(null);
            frame.setVisible(true);
        }
    }
