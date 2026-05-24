package Stakeholder_Registry is
   type Family_Record is record
      Id           : String (1 .. 32);
      Registry_Id  : String (1 .. 32);
      Renderer_Key : String (1 .. 48);
      Tranche      : String (1 .. 32);
   end record;

   Classic_Six_Count : constant Natural := 6;
   Modern_Core_Count : constant Natural := 5;
   Fallback_Mode     : constant String := "grouped-fallback";

   function Target_Name return String is ("ada-stakeholder");
   function Contract_Mode return String is ("family-focus-deterministic");
end Stakeholder_Registry;
