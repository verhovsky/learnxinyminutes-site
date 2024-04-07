
-- Τα σχόλια μιας γραμμής ξεκινούν με 2 παύλες.
{- Ενώ τα σχόλια πολλών γραμμών βρίσκονται
μέσα σε blocks σαν αυτό
-}

----------------------------------------------------
-- 1. Πρωτόγονοι Τύποι Δεδομένων (Primitive datatype) και Τελεστές
----------------------------------------------------

-- Οι αριθμοί είναι ένα primitive datatype
3 -- 3

-- Και οι τελεστές κάνουν αυτό που θα περιμέναμε
1 + 1 -- 2
8 - 1 -- 7
10 * 2 -- 20
35 / 5 -- 7.0

-- Η καθιερωμένη διαίρεση δεν είναι ακέραια
35 / 4 -- 8.75

-- Η ακέραια διαίρεση γίνεται με την συνάρτηση div
35 `div` 4 -- 8

-- Και οι boolean μεταβλητές ειναι primitives
True
False

-- Πράξεις με booleans
not True -- False
not False -- True
1 == 1 -- True
1 /= 1 -- False
1 < 10 -- True

-- Στα παραπάνω παραδείγματα, το `not` είναι μια συνάρτηση που παίρνει ένα όρισμα
-- Στην Haskell δεν χρειάζονται παρενθέσεις για τις κλήσεις συναρτήσεων, όλες οι παράμετροι
-- γράφονται με κενά αμέσως μετά την συνάρτηση. Στην γενική περίπτωση,
-- η κλήση συνάρτησης μοιάζει κάπως έτσι: func arg1 arg2 arg3...
-- Για το πως να ορίσετε τις δικές σας συναρτήσεις διαβάστε το κεφάλαιο των συναρτήσεων παρακάτω

-- Συμβολοσειρές και χαρακτήρες
"This is a string." -- συμβολοσειρά
'a' -- χαρακτήρας
'You cant use single quotes for strings.' -- error!
-- δεν μπορούμε να γράψουμε συμβολοσειρές ανάμεσα από ''

-- Οι συμβολοσειρές μπορούν να συννενωθούν με την χρήση του τελεστή ++
"Hello " ++ "world!" -- "Hello world!"

-- Η συμβολοσειρά είναι ουσιαστικά μια λίστα χαρακτήρων
['H', 'e', 'l', 'l', 'o'] -- "Hello"
"This is a string" !! 0 -- 'T'


----------------------------------------------------
-- 2. Λίστες και διατεταγμένα σύνολα (tuples)
----------------------------------------------------

-- Όλα τα στοιχεία μιας λίστας πρέπει να είναι του ίδιου τύπου
-- Οι δύο παρακάτω λίστες είναι οι ίδιες:
[1, 2, 3, 4, 5]
[1..5] -- διάστημα ή range

-- Τα διαστήματα μπορούν να χρησιμοποιηθούν και για άλλους τύπους εκτός από αριθμούς
['A'..'F'] -- "ABCDEF"

-- Μπορούμε ακόμη να ορίσουμε και ένα βήμα
[0,2..10] -- [0, 2, 4, 6, 8, 10]
[5..1] -- [] (Το default βήμα της Haskell είναι το 1, επομένως η διπλανή λίστα είναι κενή)
[5,4..1] -- [5, 4, 3, 2, 1]

-- Προσπέλαση στοιχείου σε τυχαία θέση
[1..10] !! 3 -- 4 (οι δείκτες των θέσεων ξεκινούν από το 0)

-- Στην Haskell υπάρχουν και άπειρες λίστες!
[1..] -- η λίστα των φυσικών αριθμών

-- Οι άπειρες λίστες μπορούν να λειτουργούν επειδή η Haksell έχει "lazy evaluation".
-- Αυτό σημαίνει ότι η Haskell κάνει υπολογισμούς μόνο όταν πραγματικά χρειάζεται!
-- οπότε αν ζητήσουμε το 1000στό στοιχείο μιας άπειρης λίστας θα μας το δώσει,
-- ξέρει ότι δεν χρειάζεται να υπολογίσει όλη την άπειρη λίστα πρώτα!

[1..] !! 999 -- 1000

-- Στο παραπάνω παράδειγμα η Haskell υπολόγισε τα στοιχεία 1 μέχρι 1000...τα υπόλοιπα
-- στοιχεία της άπειρης λίστας δεν υπάρχουν ακόμα! Η Haskell θα τα υπολογίσει
-- μόνο αν κάποια στιγμή τα χρειαστεί.

-- συνένωση δύο λιστών με τον τελεστή ++ (σε γραμμικό χρόνο)
[1..5] ++ [6..10]

-- προσθήκη στοιχείου στην αρχή της λίστας (σε σταθερό χρόνο)
0:[1..5] -- [0, 1, 2, 3, 4, 5]

-- περισσότερες συναρτήσεις για τις λίστες
head [1..5] -- 1
tail [1..5] -- [2, 3, 4, 5]
init [1..5] -- [1, 2, 3, 4]
last [1..5] -- 5

-- list comprehensions
-- ένας άλλος τρόπος να ορίζουμε τις λίστες που θυμίζει πολύ τον ορισμό συνόλων στα μαθηματικά!
[x*2 | x <- [1..5]] -- [2, 4, 6, 8, 10]

-- list comprehension με συνθήκη
[x*2 | x <- [1..5], x*2 > 4] -- [6, 8, 10]

-- Κάθε στοιχείο ενός tuple μπορεί να έχει διαφορετικό τύπο, όμως το tuple έχει σταθερό μέγεθος.
-- Ένα tuple:
("haskell", 1)

-- προσπέλαση στοιχείων ενός ζεύγους στοιχείων (δηλαδή ενός tuple μεγέθους 2)
fst ("haskell", 1) -- "haskell"
snd ("haskell", 1) -- 1

-- οι παραπάνω συναρτήσεις δεν λειτουργούν σε tuples μεγαλύτερου μεγέθους
snd ("snd", "can't touch this", "da na na na") -- error!

----------------------------------------------------
-- 3. Συναρτήσεις
----------------------------------------------------
-- Μια απλή συνάρτηση που παίρνει 2 μεταβλητές a, b και επιστρέφει το άθροισμά τους
add a b = a + b

-- Προσέξτε ότι αν χρησιμοποιείτε το διαδραστικό περιβάλλον της Haskell (ghci), δηλαδή
-- τον interpreter, θα πρέπει να προσθέσετε ενα `let` πριν τον ορισμό της συνάρτησης:
-- let add a b = a + b

-- Κλήση της συνάρτησης
add 1 2 -- 3

-- Μπορούμε να καλέσουμε την συνάρτηση και σαν τελεστή ανάμεσα στα 2 ορίσματα
-- γράφοντας το όνομα της συνάρτησης μέσα σε backticks:
1 `add` 2 -- 3

-- Μπορούμε να ορίσουμε και συναρτήσεις που δεν έχουν γράμματα στο όνομά τους!
-- Αυτό μας επιτρέπει να ορίσουμε δικούς μας τελεστές, όπως για παράδειγμα την ακέραια διάιρεση:

(//) a b = a `div` b
35 // 4 -- 8

-- Guards: ένας εύκολος τρόπος να υλοποιήσουμε διακλαδώσεις σε μια συνάρτηση
fib x
  | x < 2 = 1
  | otherwise = fib (x - 1) + fib (x - 2)

-- Το ταίριασμα προτύπων (Pattern matching) είναι παρόμοιο.
-- Εδώ δίνουμε 3 διαφορετικούς ορισμούς για την συνάρτηση fib
-- H Haskell θα χρησιμοποιήσει αυτόματα τον πρώτο ορισμό το οποίου οι παράμετροι
-- ταιριάζουν με τις παραμέτρους της κλήσης

fib 1 = 1
fib 2 = 2
fib x = fib (x - 1) + fib (x - 2)

-- Pattern matching σε tuples
sndOfTriple (_, y, _) = y
-- η κάτω παύλα χρησιμοποιείται για να μην δίνουμε ονόματα
-- σε μεταβλητές που δεν θα χρησιμοποιήσουμε και
-- ταιριάζει με όλους τους τύπους

-- Pattern matching σε λίστες.
-- Στο παρακάτω παράδειγμα, το `x` είναι το πρώτο στοιχείο της λίστας
-- και τo `xs` είναι η λίστα με τα υπόλοιπα στοιχεία

myMap func [] = []
myMap func (x:xs) = func x : (myMap func xs)

-- Μπορούμε να ορίσουμε και ανώνυμες συναρτήσεις (lambdas) χρησιμοποιώντας το
-- backslash (που μοιάζει με λ) ακολουθούμενο από τις παραμέτρους:
myMap (\x -> x + 2) [1..5] -- [3, 4, 5, 6, 7]

-- χρήση της συνάρτησης fold με μία ανώνυμη συνάρτηση
-- Το foldl1 είναι σαν fold από αριστερά, αλλά χρησιμοποιεί σαν αρχική τιμή του
-- accumulator το πρώτο στοιχείο της λίστας.
foldl1 (\acc x -> acc + x) [1..5] -- 15

----------------------------------------------------
-- 4. Περισσότερες συναρτήσεις
----------------------------------------------------

-- Μερική κλήση: αν δεν περάσουμε όλες τις μεταβλητές σε μια συνάρτηση,
-- τότε αυτή "καλείται μερικώς". Αυτό σημαίνει ότι μας επιστρέφει μια συνάρτηση
-- η οποία παίρνει ως ορίσματα τις εναπομείνασες μεταβλητές

add a b = a + b
foo = add 10 -- η foo είναι μια συνάρτηση που περιμένει 1 αριθμό και του προσθέτει 10
foo 5 -- 15

-- Ένας άλλος τρόπος να γράψουμε το ίδιο πράγμα:
foo = (10+)
foo 5 -- 15

-- Σύνθεση συναρτήσεων
-- Ο τελεστής `.` χρησιμοποιείται για την σύνθεση ("αλυσίδωση") συναρτήσεων.
-- Για παράδειγμα, η foo παρακάτω είναι μια συνάρτηση που παίρνει ως όρισμα 1 αριθμό.
-- Πρώτα προσθέτει 10 στον αριθμό που δώσαμε και μετά πολλαπλασιάζει το αποτέλεσμα με 4
foo = (4*) . (10+)

-- 4*(10+5) = 60
foo 5 -- 60

-- διόρθωση προτεραιότητας
-- Στην Haskell υπάρχει ο τελεστής `$`. Ο τελεστής αυτός εφαρμόζει μια συνάρτηση
-- σε μία παράμετρο. Σε αντίθεση με την απλή εφαρμογή συνάρτησης, η οποία έχει
-- την μεγαλύτερη πιθανή προτεραιότητα και είναι αριστερά προσεταιριστική,
-- ο τελεστής `$` έχει την ελάχιστη προτεραιότητας και είναι δεξιά προσεταιριστικός.
-- Λόγω της χαμηλής του προτεραιότητας, η έκφραση που βρίσκεται στα δεξιά του
-- θα υπολογιστεί και θα περαστεί σαν παράμετρος στην συνάρτηση που βρίσκεται στα αριστερά του


-- πριν
even (fib 7) -- false

-- ισοδύναμα
even $ fib 7 -- false

-- χρησιμοποιόντας σύνθεση συναρτήσεων
even . fib $ 7 -- false


----------------------------------------------------
-- 5. Τύποι
----------------------------------------------------

-- Η Haskell έχει ένα πολύ ισχυρό σύστημα τύπων, στο οποίο κάθε έκφραση έχει έναν τύπο

-- Κάποιο βασικοί τύποι:
5 :: Integer
"hello" :: String
True :: Bool

-- Και οι συναρτήσεις έχουν κάποιο τύπο
-- Η συνάρτηση`not` παίρνει ένα boolean και επιστρέφει ένα boolean:
-- not :: Bool -> Bool

-- Παρακάτω βλέπετε μια συνάρτηση που παίρνει 2 ορίσματα:
-- add :: Integer -> Integer -> Integer

-- Όταν ορίζουμε μια συνάρτηση ή μεταβλητή, είναι καλή πρακτική να γράφουμε
-- και τον τύπο της:
double :: Integer -> Integer
double x = x * 2

----------------------------------------------------
-- 6. Έλεγχος ροής και συνθήκες
----------------------------------------------------

-- if-expressions
haskell = if 1 == 1 then "awesome" else "awful" -- haskell = "awesome"

-- τα if-expressions μπορούν να πιάνουν και πολλές γραμμές
-- αλλά η στοίχιση είναι σημαντική!
haskell = if 1 == 1
            then "awesome"
            else "awful"

-- case expressions: Με τον παρακάτω τρόπο θα μπορούσαμε να κάνουμε parse
-- command line arguments
case args of
  "help" -> printHelp
  "start" -> startProgram
  _ -> putStrLn "bad args"

-- Η Haskell δεν έχει βρόχους επανάληψης; αντιθέτως, χρησιμοποιούμε αναδρομή.
-- Η συνάρτηση map εφαρμόζει μια συνάρτηση σε κάθε στοιχείο μιας λίστας

map (*2) [1..5] -- [2, 4, 6, 8, 10]

-- μπορούμε να κατασκευάσουμε τον βρόχο for χρησιμοποιώντας την map
for array func = map func array

-- και να τον χρησιμοποιήσουμε
for [0..5] $ \i -> show i

-- το παραπάνω θα μπορούσε να γραφτεί και έτσι:
for [0..5] show

-- Μπορούμε να χρησιμοποιήσουμε τις συναρτήσεις foldl και foldr
-- για να υπολογίζουμε μια τιμή από μια λίστα (πχ άθροισμα ή γινόμενο)
-- foldl <fn> <initial value> <list>
foldl (\x y -> 2*x + y) 4 [1,2,3] -- 43

-- Η παραπάνω κλήση είναι η ίδια με:
(2 * (2 * (2 * 4 + 1) + 2) + 3)

-- Η foldl γίνεται από τα αριστερά ενώ η foldr από τα δεξιά
foldr (\x y -> 2*x + y) 4 [1,2,3] -- 16

-- Η παραπάνω κλήση είναι τώρ:
(2 * 1 + (2 * 2 + (2 * 3 + 4)))

----------------------------------------------------
-- 7. Τύποι δεδομένων
----------------------------------------------------

-- Με τον παρακάτω τρόπο μπορούμε να ορίζουμε δικούς μας τύπους
-- δεδομένων στην Haskell

data Color = Red | Blue | Green

-- Τώρα μπορούμε να χρησιμοποιήσουμε τον τύπο μας και σε συναρτήσεις:

say :: Color -> String
say Red   = "You are Red!"
say Blue  = "You are Blue!"
say Green = "You are Green!"

-- Οι τύποι δεδομένων μας μπορεί να είναι και παραμετρικοί, να δέχονται δηλαδή
-- κάποιον τύπο ως παράμετρο

data Maybe a = Nothing | Just a

-- Όλες οι παρακάτω τιμές έχουν τύπο Maybe
Just "hello"    -- of type `Maybe String`
Just 1          -- of type `Maybe Int`
Nothing         -- of type `Maybe a` for any `a`

----------------------------------------------------
-- 8. Haskell IO
----------------------------------------------------

-- Αν και το IO δεν μπορεί να εξηγηθεί σε βάθος χωρίς να εξηγήσουμε
-- πρώτα τα monads, δεν είναι δύσκολο να το εξηγήσουμε αρκετά ώστε να μπορεί
-- κάποιος να το χρησιμοποιήσει

-- Όταν ένα πρόγραμμα Haskell εκτελείται, καλείται η συνάρτηση `main`
-- Η συνάρτηση αυτή πρέπει να επιστρέφει τύπο `IO a` για κάποιο τύπο `a`.
-- Για παράδειγμα:

main :: IO ()
main = putStrLn $ "Hello, sky! " ++ (say Blue)
-- η συνάρτηση putStrLn έχει τύπο: String -> IO ()

-- Είναι πιο εύκολο να χρησιμοποιήσουμε IO αν μπορούμε να γράψουμε το πρόγραμμά μας
-- ως μια συνάρτηση από String σε String. Η συνάρτηση
--    interact :: (String -> String) -> IO ()
-- παίρνει ως είσοδο ένα string, τρέχει μια συνάρτηση πάνω στην είσοδο
-- και τυπώνει την έξοδο

countLines :: String -> String
countLines = show . length . lines

main' = interact countLines

-- Μπορείτε να σκεφτείτε μια συνάρτηση που επιστρέφει τιμή με τύπο `IO ()`
-- ως μια ακολουθία πράξεων, περίπου όπως και σε μια imperative γλώσσα
-- Μπορούμε να χρησιμοποιήσουμε το `do` και να ενώσουμε αυτές τις κλήσεις
-- Για παράδειγμα:

sayHello :: IO ()
sayHello = do
   putStrLn "What is your name?"
   name <- getLine -- η συνάρτηση αυτή διαβάζει μια γραμμή και την αναθέτει στην μετβαλήτη name
   putStrLn $ "Hello, " ++ name

-- Δοκιμάστε να γράψετε την συνάρτηση `interact` που θα διαβάζει μια γραμμή

-- Ωστόσο ο κώδικας της συνάρτησης `sayHello` δεν θα εκτελεστεί ποτέ. Η μόνη συνάρτηση
-- που εκτελείται όταν κάνουμε compile ένα αρχείο haskell είναι η `main`.
-- Αν θέλετε να τρέξετε την sayHello (εκτός από το να φορτώσετε τον κώδικα στο
-- ghci) μπορείτε να βάλετε σε σχόλια τον προηγούμενο ορισμό της main
-- και να την ορίσετε ως:
--    main = sayHello

-- Ας προσπαθήσουμε να καταλάβουμε πως λειτουργεί η συνάρτηση `getLine`
-- Ο τύπος της είναι:
--    getLine :: IO String
-- Μπορείτε να φανταστείτε ότι μια τιμή με τύπο `IO a` θα παραχθεί
-- από ένα πρόγραμμα που παράγει μια τιμή με τύπο `a` (ενώ παράλληλα κάνει και κάτι άλλο)
-- Μπορούμε να πάρουμε και να επαναχρησιμοποιήσουμε αυτήν την τιμή χρησιμοποιώντας
-- το `<-`. Μπορούμε ακόμα και να φτιάξουμε την δική μας συνάρτηση με τύπο
-- `IO String`:

action :: IO String
action = do
   putStrLn "This is a line. Duh"
   input1 <- getLine
   input2 <- getLine
   -- Ο τύπος του `do` μπλοκ είναι εκείνος της τελευταίας γραμμής.
   -- Το `return` δεν είναι κάποια ειδική λέξη, αλλά απλώς μια συνάρτηση
   return (input1 ++ "\n" ++ input2) -- return :: String -> IO String

-- Μπορούμε να χρησιμοποιήσουμε την παραπάνω συνάρτηση ακριβώς όπως την  `getLine`:

main'' = do
    putStrLn "I will echo two lines!"
    result <- action
    putStrLn result
    putStrLn "This was all, folks!"

-- Ο τύπος `IO` είναι παράδειγμα ενός "monad". Χρησιμοποιώντας τα monads για το
-- ΙΟ, η Haskell καταφέρνει να είναι αγνή συναρτησιακή γλώσσα. Κάθε συνάρτηση που
-- αλληλεπιδρά με τον έξω κόσμο (δηλαδή κάνει IO), έχει το IO (ή κάποιο άλλο monad)
-- στον τύπο της. Αυτό μας διευκολύνει να γνωρίζουμε ποιές συναρτήσεις είναι αγνές
-- (μαθηματικές -- δεν αλληλεπιδρούν με τον έξω κόσμο ούτε αλλάζουν κάποιο state)
-- και ποιες δεν είναι.

-- Αυτό είναι ένα πολύ ισχυρό χαρακτηριστικό γιατί είναι πολύ εύκολο να
-- εκτελούμε παράλληλα αγνές συναρτήσεις! Οπότε η παραλληλοποίηση στην Haskell
-- είναι αρκετά πιο εύκολη

----------------------------------------------------
-- 9. Haskell REPL
----------------------------------------------------

-- Μπορείτε να ξεκινήσετε το διαδραστικό περιβάλλον της Haskell με την εντολή `ghci`.
-- Εδώ μπορείτε να γράψετε και να εκτελέσετε κώδικα haskell.
-- Κάθε νέα τιμή πρέπει να ορίζεται με το `let`

let foo = 5

-- Μπορείτε να βρείτε τον τύπο μιας συνάρτησης με το `:t`:

> :t foo
foo :: Integer

-- Οι τελεστές, όπως οι `+`, `:` και `$`, είναι επίσης συναρτήσεις.
-- Μπορούμε να δούμε τον τύπο τους βάζοντας τους μέσα σε παρενθέσεις:

> :t (:)
(:) :: a -> [a] -> [a]

-- Για περισσότερες πληροφορίες για οποιαδήποτε συνάρτηση ή τύπο,
-- μπορείτε να χρησιμοποιήσετε το `:i`:

> :i (+)
class Num a where
  (+) :: a -> a -> a
  ...
    -- Defined in ‘GHC.Num’
infixl 6 +

-- Μπορείτε επίσης να τρέξετε κάθε συνάρτηση με τύπο `IO ()`

> sayHello
What is your name?
Friend!
Hello, Friend!

qsort [] = []
qsort (p:xs) = qsort lesser ++ [p] ++ qsort greater
    where lesser  = filter (< p) xs
          greater = filter (>= p) xs

