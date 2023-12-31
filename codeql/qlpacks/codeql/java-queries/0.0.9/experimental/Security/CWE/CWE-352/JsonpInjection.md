# JSONP Injection
The software uses external input as the function name to wrap JSON data and returns it to the client as a request response. When there is a cross-domain problem, this could lead to information leakage.


## Recommendation
Adding `Referer`/`Origin` or random `token` verification processing can effectively prevent the leakage of sensitive information.


## Example
The following examples show the bad case and the good case respectively. Bad cases, such as `bad1` to `bad7`, will cause information leakage when there are cross-domain problems. In a good case, for example, in the `good1` method and the `good2` method, When these two methods process the request, there must be a request body in the request, which does not meet the conditions of Jsonp injection.


```java
import com.alibaba.fastjson.JSONObject;
import com.fasterxml.jackson.databind.ObjectMapper;
import com.google.gson.Gson;
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.util.HashMap;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.ResponseBody;
import org.springframework.web.multipart.MultipartFile;

@Controller
public class JsonpInjection {

    private static HashMap hashMap = new HashMap();

    static {
        hashMap.put("username","admin");
        hashMap.put("password","123456");
    }

    @GetMapping(value = "jsonp1")
    @ResponseBody
    public String bad1(HttpServletRequest request) {
        String resultStr = null;
        String jsonpCallback = request.getParameter("jsonpCallback");
        Gson gson = new Gson();
        String result = gson.toJson(hashMap);
        resultStr = jsonpCallback + "(" + result + ")";
        return resultStr;
    }

    @GetMapping(value = "jsonp2")
    @ResponseBody
    public String bad2(HttpServletRequest request) {
        String resultStr = null;
        String jsonpCallback = request.getParameter("jsonpCallback");
        resultStr = jsonpCallback + "(" + JSONObject.toJSONString(hashMap) + ")";
        return resultStr;
    }

    @GetMapping(value = "jsonp3")
    @ResponseBody
    public String bad3(HttpServletRequest request) {
        String resultStr = null;
        String jsonpCallback = request.getParameter("jsonpCallback");
        String jsonStr = getJsonStr(hashMap);
        resultStr = jsonpCallback + "(" + jsonStr + ")";
        return resultStr;
    }

    @GetMapping(value = "jsonp4")
    @ResponseBody
    public String bad4(HttpServletRequest request) {
        String resultStr = null;
        String jsonpCallback = request.getParameter("jsonpCallback");
        String restr = JSONObject.toJSONString(hashMap);
        resultStr = jsonpCallback + "(" + restr + ");";
        return resultStr;
    }

    @GetMapping(value = "jsonp5")
    @ResponseBody
    public void bad5(HttpServletRequest request,
            HttpServletResponse response) throws Exception {
        String jsonpCallback = request.getParameter("jsonpCallback");
        PrintWriter pw = null;
        Gson gson = new Gson();
        String result = gson.toJson(hashMap);
        String resultStr = null;
        pw = response.getWriter();
        resultStr = jsonpCallback + "(" + result + ")";
        pw.println(resultStr);
    }

    @GetMapping(value = "jsonp6")
    @ResponseBody
    public void bad6(HttpServletRequest request,
            HttpServletResponse response) throws Exception {
        String jsonpCallback = request.getParameter("jsonpCallback");
        PrintWriter pw = null;
        ObjectMapper mapper = new ObjectMapper();
        String result = mapper.writeValueAsString(hashMap);
        String resultStr = null;
        pw = response.getWriter();
        resultStr = jsonpCallback + "(" + result + ")";
        pw.println(resultStr);
    }

    @RequestMapping(value = "jsonp7", method = RequestMethod.GET)
    @ResponseBody
    public String bad7(HttpServletRequest request) {
        String resultStr = null;
        String jsonpCallback = request.getParameter("jsonpCallback");
        Gson gson = new Gson();
        String result = gson.toJson(hashMap);
        resultStr = jsonpCallback + "(" + result + ")";
        return resultStr;
    }

    @RequestMapping(value = "jsonp11")
    @ResponseBody
    public String good1(HttpServletRequest request) {
        JSONObject parameterObj = readToJSONObect(request);
        String resultStr = null;
        String jsonpCallback = request.getParameter("jsonpCallback");
        String restr = JSONObject.toJSONString(hashMap);
        resultStr = jsonpCallback + "(" + restr + ");";
        return resultStr;
    }

    @RequestMapping(value = "jsonp12")
    @ResponseBody
    public String good2(@RequestParam("file") MultipartFile file,HttpServletRequest request) {
        if(null == file){
            return "upload file error";
        }
        String fileName = file.getOriginalFilename();
        System.out.println("file operations");
        String resultStr = null;
        String jsonpCallback = request.getParameter("jsonpCallback");
        String restr = JSONObject.toJSONString(hashMap);
        resultStr = jsonpCallback + "(" + restr + ");";
        return resultStr;
    }

    public static JSONObject readToJSONObect(HttpServletRequest request){
        String jsonText = readPostContent(request);
        JSONObject jsonObj = JSONObject.parseObject(jsonText, JSONObject.class);
        return jsonObj;
    }

    public static String readPostContent(HttpServletRequest request){
        BufferedReader in= null;
        String content = null;
        String line = null;
        try {
            in = new BufferedReader(new InputStreamReader(request.getInputStream(),"UTF-8"));
            StringBuilder buf = new StringBuilder();
            while ((line = in.readLine()) != null) {
                buf.append(line);
            }
            content = buf.toString();
        } catch (IOException e) {
            e.printStackTrace();
        }
        String uri = request.getRequestURI();
        return content;
    }

    public static String getJsonStr(Object result) {
        return JSONObject.toJSONString(result);
    }
}
```

## References
* OWASPLondon20161124_JSON_Hijacking_Gareth_Heyes: [JSON hijacking](https://owasp.org/www-chapter-london/assets/slides/OWASPLondon20161124_JSON_Hijacking_Gareth_Heyes.pdf).
* Practical JSONP Injection: [ Completely controllable from the URL (GET variable) ](https://securitycafe.ro/2017/01/18/practical-jsonp-injection).
* Common Weakness Enumeration: [CWE-352](https://cwe.mitre.org/data/definitions/352.html).
