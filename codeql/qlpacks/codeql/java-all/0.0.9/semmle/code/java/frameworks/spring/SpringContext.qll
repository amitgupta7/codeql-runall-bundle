/**
 * Provides models for the `org.springframework.context` package.
 */

import java
private import semmle.code.java.dataflow.ExternalFlow

private class StringSummaryCsv extends SummaryModelCsv {
  override predicate row(string row) {
    row =
      [
        //`namespace; type; subtypes; name; signature; ext; input; output; kind`
        "org.springframework.context;MessageSource;true;getMessage;(String,Object[],String,Locale);;ArrayElement of Argument[1];ReturnValue;taint",
        "org.springframework.context;MessageSource;true;getMessage;(String,Object[],String,Locale);;Argument[2];ReturnValue;taint",
        "org.springframework.context;MessageSource;true;getMessage;(String,Object[],Locale);;ArrayElement of Argument[1];ReturnValue;taint"
      ]
  }
}
