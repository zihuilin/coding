package javaWeek7;

import java.awt.BorderLayout;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.io.File;

import javax.swing.JButton;
import javax.swing.JFileChooser;
import javax.swing.JFrame;
import javax.swing.JTextArea;

public class FileChooserDemo extends JFrame{
	
	private JButton chooseButton = new JButton("Choose File");
	private JTextArea displayArea = new JTextArea(5, 10);
	
	public FileChooserDemo() {
		this.setLayout(new BorderLayout());
		this.add(chooseButton, BorderLayout.NORTH);
		this.add(displayArea, BorderLayout.CENTER);
		
		chooseButton.addActionListener(new ActionListener() {
			
			@Override
			public void actionPerformed(ActionEvent arg0) {
				JFileChooser fileChooser = new JFileChooser();
				int returnValue = fileChooser.showOpenDialog(null);
				if (returnValue == JFileChooser.APPROVE_OPTION) {
					File file = fileChooser.getSelectedFile();
					displayArea.append(file.getPath() + "\n");
					file.renameTo(new File(file.getPath()+"(renamed)"));
				}
			}
		});
		
		this.pack();
		this.setVisible(true);
		this.setLocationRelativeTo(null);
		this.setDefaultCloseOperation(EXIT_ON_CLOSE);
	}

	public static void main(String[] args) {
		new FileChooserDemo();

	}

}
