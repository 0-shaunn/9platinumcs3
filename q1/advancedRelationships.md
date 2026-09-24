# Advanced Class Relationships
## Previous Activities
[classAttributesMethods](classAttributesMethods.md)

[classRelationships](classRelationships.md)
## Existing System Description: 
The existing system manages a variety of ⁠Anime⁠ series within a ⁠StreamingService⁠ catalog using basic association and multiplicity.
## Inheritance Relationship
Parent: Anime

Child: ShojoAnime

Explanation: ShojoAnime⁠ IS-A specific demographic type of ⁠Anime⁠. It inherits general media properties like title, episodes, source, and duration, along with an additional ⁠romance_subgenre⁠ attribute.
## Inheritance UML
![Inheritance](images/inheritanceDiagram.png)
## Composition/Aggregation
Relationship: Aggregation (⁠StreamingService⁠ ◇── ⁠Anime⁠)

Explanation: This is Aggregation because the ⁠Anime⁠ objects exist independently and will not be destroyed if the ⁠StreamingService⁠ instance is removed.
## Advanced UML Diagram
![Advanced UML](images/advancedClassDiagram.png)
## Python Implementation
[Source Code](advancedRelationships.py)
## Test Run
![Test](images/advancedTestRun.png)
## Object Diagram
![Objects](images/advancedObjectDiagram.png)
## Reflection
Answers:

1. I chose ⁠ShojoAnime⁠ as a child class of ⁠Anime⁠ because a shojo series IS-A specialized demographic of anime. It contains common attributes such as title, episode count, source material, and duration with standard anime series, but adds genre-specific attributes such as romance subgenres.

2. Inheritance reduced duplicate code as it allowed ⁠ShojoAnime⁠ to inherit all attributes and playback methods directly from ⁠Anime⁠. By calling ⁠super().__init__()⁠, the child class reuses the parent's initialization instead of re-declaring attributes.

3. My HAS-A relationship is Aggregation because ⁠StreamingService⁠ contains a catalog of ⁠Anime⁠ objects that can exist independently. If a streaming service goes offline or does not exist entirely, the ⁠Anime⁠ series instances still exist separately.

4. The general association from Part III showed a usage connection between independent classes. On the other hand, the advanced relationships represent structural specialization through Inheritance and ownership structure through Aggregation.

5. My design follows the DRY (Don't Repeat Yourself) principle through concentrating core media attributes and methods inside the parent ⁠Anime⁠ class. Furthermore, classes like ⁠ShojoAnime⁠ extend this functionality without duplicating code.

