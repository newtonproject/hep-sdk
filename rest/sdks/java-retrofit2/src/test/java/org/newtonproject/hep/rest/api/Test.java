package org.newtonproject.hep.rest.api;

import sun.reflect.annotation.ExceptionProxy;

public class Test {
    @org.junit.Test
    public void StringTest() throws Exception {
        String a = "111";
        String b = "122";
        int i = a.compareTo(b);
        System.out.println(i);
    }
}
