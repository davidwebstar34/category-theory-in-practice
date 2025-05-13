module CategoryBasics where

identity :: a -> a
identity x = x

compose :: (b -> c) -> (a -> b) -> a -> c
compose g f = \x -> g (f x)

leftIdentity :: (a -> b) -> a -> b
leftIdentity f = compose f identity

rightIdentity :: (a -> b) -> a -> b
rightIdentity f = compose identity f