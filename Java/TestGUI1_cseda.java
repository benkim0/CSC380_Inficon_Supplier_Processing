

import javax.swing.*;
import javax.swing.filechooser.FileNameExtensionFilter;
import javax.swing.filechooser.FileSystemView;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.io.File;
import java.io.IOException;
import java.util.ArrayList;
import java.util.Arrays;

public class TestGUI1_cseda {
    JFrame frame;
    ArrayList<File> inputFiles;
    JPanel filePanel;
    JScrollPane filePane;
    JButton logoutButton;
    JFileChooser fc;


    public TestGUI1_cseda(){
        createGUI();
    }

    private void createGUI() {
        inputFiles = new ArrayList<>();
        filePanel = new JPanel();
        frame = new JFrame("Test");
        fc = new JFileChooser();

        filePanel.setLayout(new BoxLayout(filePanel,BoxLayout.Y_AXIS));

        filePane = new JScrollPane(filePanel);
        filePane.setBounds(230,30,400,400);



        frame.add(filePane);
        frame.setSize(1200,720);
        frame.setLayout(null);
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setVisible(true);


    }

    public void buttonFunct(){
        JButton uploadButton = new JButton("Upload");

        JButton fillButton = new JButton("Fill");
        fillButton.setEnabled(false);

        uploadButton.setBounds(30,30,200,30);
        fillButton.setBounds(30,60,200,30);
        //String defaultDir = FileSystemView.getFileSystemView().getHomeDirectory() + File.separator + "Documents";


        uploadButton.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {

                FileDialog fd = new FileDialog(frame, "Select file");
                fd.setMultipleMode(true);
                fd.setVisible(true);
                File[] files = fd.getFiles();

                inputFiles.addAll(Arrays.asList(files));

                for(File file : files) {
                    JLabel l = new JLabel(file.getName());
                    filePanel.add(l);


                }
                frame.setVisible(true);
                fillButton.setEnabled(true);

            }
        });
        fillButton.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {

                for(File file : inputFiles){
                    ProcessBuilder pBuilder = new ProcessBuilder("C:\\Users\\super\\AppData\\Local\\Programs\\Python\\Python314\\python.exe", "C:\\Users\\super\\ForFunsies\\CSC380_Inficon_Supplier_Processing\\Python\\guitest.py",file.getAbsolutePath());
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
                frame.setVisible(true);

            }
        });

        frame.add(uploadButton);
        frame.add(fillButton);

        frame.update(frame.getGraphics());
    }

        public static void main( String[] args) throws IOException {
            TestGUI1_cseda c = new TestGUI1_cseda();
            c.buttonFunct();

        }
    }
