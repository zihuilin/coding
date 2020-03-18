import java.util.Scanner;

public class Point {
	//声明有关点的数据
	/**
	 * 成员变量：x, 横坐标
	 */
	float x;
	
	/**
	 * 成员变量：y, 纵坐标
	 */
	float y;
	
	public Point(float x, float y) {
		this.x = x;
		this.y = y;
	}
	
	public float getX() {
		return x;
	}
	
	public float getY() {
		return y;
	}
	
	public void setX(float x){
		this.x = x;
	}
	
	public void setY(float y){
		this.y = y;
	}
	
	public float getDistance(Point p) {
		return (float)Math.sqrt(
				(this.x-p.x)*(this.x-p.x) + 
				(this.y-p.y)*(this.y-p.y) );
	}

	public static void main(String[] args) {		
		Point p1 = new Point(10, 20);
		Point p2 = new Point(20, 20);
		
		System.out.println(p1.getDistance(p2));
		
//		float distance = (float)Math.sqrt(
//				(p1.x-p2.x)*(p1.x-p2.x) + (p1.y-p2.y)*(p1.y-p2.y) ); 
//		p.x = 10;
//		p.y = 20;
		
//		System.out.println(p.getX());
//		System.out.println(p.x);
	}

}
