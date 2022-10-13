from kanren import run, var, eq, Relation, facts
a = var()
b = var()

padre = Relation()
primo = Relation()
tio = Relation()
facts(padre, ("Mario V","Jaqueline V"),("Mario V","Eli V"),("Mario V","Miguel V"),("Mario V","Edgar V"),
      ("Mario H","Esperanza H"),("Mario H","Miriam H"),("Mario H","Adhemar H"), ("Mario H","Marco H"),
      ("Adhemar H","Sergio H"),("Adhemar H","Pablo H"), ("Adhemar H","Andrea H"))
facts(primo, ("Sergio H","Jorge C"),("Pablo H","Jorge C"),("Andrea H","Jorge C"),
      ("Sergio H","Ericka P"),("Pablo H","Ericka P"),("Andrea H","Ericka P"),
      ("Sergio H","Lorena Pr"),("Pablo H","Lorena Pr"),("Andrea H","Lorena Pr"))
facts(tio, ("Esperanza H","Sergio H"),("Marco H","Sergio H"),("Miguel V","Sergio H"),
      ("Eli V","Pablo H"),("Eli V","Andrea H"),("Miguel V","Andrea H"))

print(padre.facts)
print(run(1,a,padre(a,"Adhemar H")))
print(run(1,a,padre(a,"Sergio H")))
print(run(4,b,padre("Mario H",b)))
print(run(3,b,padre("Mario V",b)))
print(run(3,b,padre("Adhemar H",b)))

print("primos")
print(run(3,a,primo(a,"Lorena Pr")))
print(run(3,a,primo(a,"Ericka P")))
print(run(3,a,primo(a,"Jorge C")))
print(run(3,a,primo("Sergio H",a)))
print(run(3,a,primo("Pablo H",a)))
print(run(3,a,primo("Andrea H",a)))

print("relacion tios")
print(run(2,a,tio(a,"Andrea H")))
print(run(3,a,tio(a,"Sergio H")))