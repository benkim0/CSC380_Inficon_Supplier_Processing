import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.io.File;
import java.io.IOException;
import java.util.ArrayList;
import java.util.Arrays;

public class TestGUI1_cseda {

        public static void main( String[] args) throws IOException {
            ArrayList<File> inputFiles = new ArrayList<>();
            ArrayList<File> outputFiles = new ArrayList<>();

            JFrame frame = new JFrame("Test");
            JButton uploadButton = new JButton("Upload");

            JButton fillButton = new JButton("Fill");
            fillButton.setEnabled(false);

            uploadButton.setBounds(30,30,200,30);
            fillButton.setBounds(30,60,200,30);

            frame.add(uploadButton);
            frame.add(fillButton);

            frame.setSize(1200,720);
            frame.setLayout(null);
            frame.setVisible(true);


            uploadButton.addActionListener(new ActionListener() {
                @Override
                public void actionPerformed(ActionEvent e) {
                    FileDialog fd = new FileDialog(frame);

                    fd.setMultipleMode(true);
                    fd.setVisible(true);

                    File [] files = fd.getFiles();
                    inputFiles.addAll(Arrays.asList(files));
                    fillButton.setEnabled(!inputFiles.isEmpty());

                }
            });
            fillButton.addActionListener(new ActionListener() {
                @Override
                public void actionPerformed(ActionEvent e) {

                    for(File file : inputFiles){
                        ProcessBuilder pBuilder = new ProcessBuilder("C:\\Users\\super\\AppData\\Local\\Programs\\Python\\Python314\\python.exe", "C:\\Users\\super\\ForFunsies\\CSC380_Inficon_Supplier_Processing\\Python\\main.py",file.getAbsolutePath());
                        pBuilder.redirectOutput(ProcessBuilder.Redirect.INHERIT);

                        try {
                            Process p = pBuilder.start();

                        }
                        catch (IOException ex) {
                            throw new RuntimeException(ex);
                        }

                    }
                    inputFiles.clear();
                    fillButton.setEnabled(false);

                }
            });

        }
    }
