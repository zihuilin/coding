public class FloatEqual{

    public static void main(String[] args){
        //1. float的精度“不足”：你觉得并不相等，但却“相等”
        /*
        float f = 9.9999999f;
        int i = 10;
        if (i > f)
            System.out.println("i>f");
        else
            System.out.println("i<=f");
            */

        //2. double的精度"过高"：你觉得应该相等，但却“不相等”
        //面积为10的圆的半径是多少？
        /*
        double r = 1.784124111;
        double s = Math.PI*r*r;
        System.out.println("s=" + s);
        if (s == 10)
            System.out.println("半径为r的圆的面积是10");
        else
            System.out.println("半径为r的圆的面积不是10");
            */
        //3. 浮点数的“相等”要引入一个“误差范围”
        double e = 0.0000001;
        double r = 1.784124111;
        double s = Math.PI*r*r;
        System.out.println("s=" + s);
        if (Math.abs(s - 10) < e)
            System.out.println("半径为r的圆的面积是10");
        else
            System.out.println("半径为r的圆的面积不是10");

    }
}
